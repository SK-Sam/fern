import { assertNever } from "@fern-api/core-utils";
import { TaskContext } from "@fern-api/task-context";
import {
    ExampleEndpointCall,
    ExamplePathParameter,
    ExampleTypeReference,
    HttpEndpoint,
    IntermediateRepresentation,
    NameAndWireValue
} from "@fern-fern/ir-sdk/api";
import express, { Request, Response } from "express";
import getPort from "get-port";
import { IncomingHttpHeaders } from "http";
import { isEqual } from "lodash-es";
import qs from "qs";
import urlJoin from "url-join";

type RequestHandler = (req: Request, res: Response) => void;

// TODO: There are a few gaps in what the mock server can
// validate, which will require changes to the example IR.
//
// See https://github.com/fern-api/fern/issues/2620
export async function runMockServer({
    context,
    ir,
    port
}: {
    context: TaskContext;
    ir: IntermediateRepresentation;
    port: number | undefined;
}): Promise<void> {
    const app = express();
    app.use(express.json({ limit: "50mb", strict: false }));

    for (const service of Object.values(ir.services)) {
        for (const endpoint of service.endpoints) {
            const endpointPath = getFullPathForEndpoint(endpoint);
            context.logger.info(`Registering ${endpoint.method} ${endpointPath} ...`);
            switch (endpoint.method) {
                case "GET":
                    app.get(endpointPath, getRequestHandler(endpoint));
                    break;
                case "POST":
                    app.post(endpointPath, getRequestHandler(endpoint));
                    break;
                case "PUT":
                    app.put(endpointPath, getRequestHandler(endpoint));
                    break;
                case "PATCH":
                    app.patch(endpointPath, getRequestHandler(endpoint));
                    break;
                case "DELETE":
                    app.delete(endpointPath, getRequestHandler(endpoint));
                    break;
                default:
                    assertNever(endpoint.method);
            }
        }
    }

    if (port == null) {
        port = await getPort();
    }
    app.listen(port);

    context.logger.info(`Running mock server on localhost:${port}`);

    // await infiinitely
    // eslint-disable-next-line @typescript-eslint/no-empty-function
    await new Promise(() => {});
}

function getFullPathForEndpoint(endpoint: HttpEndpoint): string {
    let url = "";
    if (endpoint.fullPath.head.length > 0) {
        url = urlJoin(url, endpoint.fullPath.head);
    }
    for (const part of endpoint.fullPath.parts) {
        // Unlike the Fern IR, express expects the ':'
        // token to specify a path parameter.
        //
        //  /movie/:movieId
        //
        url = urlJoin(url, ":" + part.pathParameter);
        if (part.tail.length > 0) {
            url = urlJoin(url, part.tail);
        }
    }
    return url.startsWith("/") ? url : `/${url}`;
}

function getRequestHandler(endpoint: HttpEndpoint): RequestHandler {
    return (req: Request, res: Response) => {
        if (endpoint.examples.length === 0) {
            res.status(500).send("This endpoint doesn't have any examples");
            return;
        }
        for (const example of endpoint.examples) {
            if (isRequestMatch(req, example)) {
                if (example.response.body == null) {
                    res.sendStatus(200);
                    return;
                }
                res.json(example.response.body.jsonExample);
                return;
            }
        }
        res.status(404).send("Unrecognized example request");
    };
}

function isRequestMatch(req: Request, example: ExampleEndpointCall): boolean {
    return (
        validatePathParameters(example, req) &&
        validateQueryParameters(example, req) &&
        validateHeaders(example, req.headers) &&
        validateRequestBody(example, req)
    );
}

function validatePathParameters(example: ExampleEndpointCall, req: Request): boolean {
    const examplePathParameters = examplePathParametersToRecord([
        ...example.rootPathParameters,
        ...example.servicePathParameters,
        ...example.endpointPathParameters
    ]);
    if (Object.keys(examplePathParameters).length !== Object.keys(req.params).length) {
        return false;
    }
    if (Object.keys(examplePathParameters).length > 0) {
        if (!isEqual(req.params, examplePathParameters)) {
            return false;
        }
    }
    return true;
}

function validateQueryParameters(example: ExampleEndpointCall, req: Request): boolean {
    const exampleQueryParameters = examplesWithWireValueToRecord(example.queryParameters);
    if (Object.keys(exampleQueryParameters).length !== Object.keys(req.query).length) {
        return false;
    }
    if (Object.keys(exampleQueryParameters).length > 0) {
        return stringifyQuery(req.query) === stringifyQuery(exampleQueryParameters);
    }
    return true;
}

function validateHeaders(example: ExampleEndpointCall, headers: IncomingHttpHeaders): boolean {
    // For headers, we're slightly more permissive. We allow more headers
    // than what are specified in the example (e.g. Accept, Content-Type, etc).
    const exampleHeaders = examplesWithWireValueToRecord([...example.serviceHeaders, ...example.endpointHeaders]);
    for (const [key, value] of Object.entries(exampleHeaders)) {
        if (headers[key.toLowerCase()] !== (value as string)) {
            return false;
        }
    }
    return true;
}

function validateRequestBody(example: ExampleEndpointCall, req: Request): boolean {
    if (example.request == null) {
        // By default, express interprets an empty request body as '{}'.
        return isObject(req.body) && Object.keys(req.body).length === 0;
    }
    return isEqual(req.body, example.request.jsonExample);
}

// ExampleWithWireValue is implemented by both example headers and example query parameters.
interface ExampleWithWireValue {
    name: NameAndWireValue;
    value: ExampleTypeReference;
}

function examplesWithWireValueToRecord(examplesWithWireValue: ExampleWithWireValue[]): Record<string, unknown> {
    const result: Record<string, unknown> = {};
    examplesWithWireValue.forEach((exampleWithWireValue) => {
        result[exampleWithWireValue.name.wireValue] = exampleWithWireValue.value.jsonExample;
    });
    return result;
}

function examplePathParametersToRecord(examplePathParameters: ExamplePathParameter[]): Record<string, unknown> {
    const result: Record<string, unknown> = {};
    examplePathParameters.forEach((examplePathParameter) => {
        result[examplePathParameter.name.originalName] = examplePathParameter.value.jsonExample;
    });
    return result;
}

function stringifyQuery(q: unknown): string {
    return qs.stringify(q, {
        arrayFormat: "repeat",
        sort: (a, b) => {
            return a > b ? 0 : 1;
        }
    });
}

function isObject(value: unknown): value is object {
    return typeof value === "object" && value != null;
}
