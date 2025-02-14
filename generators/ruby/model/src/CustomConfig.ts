import { BaseGeneratorConfigSchema } from "@fern-api/generator-commons";
import { z } from "zod";

export type RubyModelCustomConfig = z.infer<typeof RubyModelCustomConfigSchema>;
export const RubyModelCustomConfigSchema = BaseGeneratorConfigSchema.extend({
    gemName: z.optional(z.string())
});

// TODO: this will likely be shared between models and SDK
export function parseCustomConfig(customConfig: unknown): RubyModelCustomConfig {
    const parsed = customConfig != null ? RubyModelCustomConfigSchema.parse(customConfig) : undefined;
    return {
        defaultTimeoutInSeconds: parsed?.defaultTimeoutInSeconds ?? parsed?.defaultTimeoutInSeconds,
        extraDependencies: parsed?.extraDependencies ?? {},
        clientClassName: parsed?.clientClassName,
        gemName: parsed?.gemName
    };
}
