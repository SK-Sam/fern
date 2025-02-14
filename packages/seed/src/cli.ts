import { AbsoluteFilePath, join, RelativeFilePath } from "@fern-api/fs-utils";
import { CONSOLE_LOGGER, LogLevel, LOG_LEVELS } from "@fern-api/logger";
import { loggingExeca } from "@fern-api/logging-execa";
import path from "path";
import yargs, { Argv } from "yargs";
import { hideBin } from "yargs/helpers";
import { TaskContextFactory } from "./commands/test/TaskContextFactory";
import { testCustomFixture } from "./commands/test/testCustomFixture";
import { FIXTURES, testWorkspaceFixtures } from "./commands/test/testWorkspaceFixtures";
import { loadSeedWorkspaces } from "./loadSeedWorkspaces";

void tryRunCli();

export async function tryRunCli(): Promise<void> {
    const cli: Argv = yargs(hideBin(process.argv));

    addTestCommand(cli);

    await cli.parse();

    CONSOLE_LOGGER.info("Seed has finished...");
}

function addTestCommand(cli: Argv) {
    cli.command(
        "test",
        "Run all snapshot tests",
        (yargs) =>
            yargs
                .option("workspace", {
                    type: "string"
                })
                .option("parallel", {
                    type: "number",
                    default: 4
                })
                .option("custom-fixture", {
                    type: "string",
                    demandOption: false,
                    description: "Path to the api directory"
                })
                .option("fixture", {
                    type: "string",
                    choices: FIXTURES,
                    demandOption: false,
                    description: "Runs on all fixtures if not provided"
                })
                .option("update", {
                    type: "boolean",
                    alias: "u",
                    description: "Determines whether or not snapshots are written to disk",
                    default: false
                })
                .option("log-level", {
                    default: LogLevel.Info,
                    choices: LOG_LEVELS
                }),
        async (argv) => {
            const workspaces = await loadSeedWorkspaces();

            const filteredWorkspace = workspaces.filter((workspace) => {
                return workspace.workspaceName === argv.workspace;
            });

            if (filteredWorkspace[0] == null) {
                throw new Error(`Failed to find workspace ${argv.workspace}`);
            }

            const workspace = filteredWorkspace[0];

            const parsedDockerImage = validateAndParseDockerImage(workspace.workspaceConfig.docker);

            // build docker iamge
            const taskContextFactory = new TaskContextFactory(argv["log-level"]);
            const dockerCommand = workspace.workspaceConfig.dockerCommand;
            if (dockerCommand != null) {
                const workspaceTaskContext = taskContextFactory.create(workspace.workspaceName);
                const spaceDelimitedCommand = dockerCommand.split(" ");
                await loggingExeca(
                    workspaceTaskContext.logger,
                    spaceDelimitedCommand[0] ?? dockerCommand,
                    spaceDelimitedCommand.slice(1),
                    {
                        cwd: path.dirname(path.dirname(workspace.absolutePathToWorkspace)),
                        doNotPipeOutput: false
                    }
                );
            }

            if (argv.customFixture != null) {
                await testCustomFixture({
                    pathToFixture: argv.customFixture.startsWith("/")
                        ? AbsoluteFilePath.of(argv.customFixture)
                        : join(AbsoluteFilePath.of(__dirname), RelativeFilePath.of(argv.customFixture)),
                    workspace,
                    irVersion: workspace.workspaceConfig.irVersion,
                    language: workspace.workspaceConfig.language,
                    docker: parsedDockerImage,
                    logLevel: argv["log-level"],
                    numDockers: argv.parallel
                });
            } else {
                await testWorkspaceFixtures({
                    workspace,
                    fixtures: argv.fixture != null ? [argv.fixture] : FIXTURES,
                    irVersion: workspace.workspaceConfig.irVersion,
                    language: workspace.workspaceConfig.language,
                    docker: parsedDockerImage,
                    dockerCommand: workspace.workspaceConfig.dockerCommand,
                    scripts: workspace.workspaceConfig.scripts,
                    logLevel: argv["log-level"],
                    numDockers: argv.parallel,
                    taskContextFactory
                });
            }
        }
    );
}

export interface ParsedDockerName {
    name: string;
    version: string;
}

function validateAndParseDockerImage(docker: string): ParsedDockerName {
    const dockerArray: string[] = docker.split(":");
    if (dockerArray.length === 2 && dockerArray[0] != null && dockerArray[1] != null) {
        return {
            name: dockerArray[0],
            version: dockerArray[1]
        };
    }
    throw new Error(`Received invalid docker name ${docker}. Must be formatted as <name>:<version>`);
}
