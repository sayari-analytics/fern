/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";

export const CreateProblemResponse: core.serialization.Schema<
    serializers.CreateProblemResponse.Raw,
    SeedTrace.CreateProblemResponse
> = core.serialization
    .union("type", {
        success: core.serialization.object({
            value: core.serialization.lazy(async () => (await import("../../..")).ProblemId),
        }),
        error: core.serialization.object({
            value: core.serialization.lazy(async () => (await import("../../..")).CreateProblemError),
        }),
    })
    .transform<SeedTrace.CreateProblemResponse>({
        transform: (value) => {
            switch (value.type) {
                case "success":
                    return SeedTrace.CreateProblemResponse.success(value.value);
                case "error":
                    return SeedTrace.CreateProblemResponse.error(value.value);
                default:
                    return SeedTrace.CreateProblemResponse._unknown(value);
            }
        },
        untransform: ({ _visit, ...value }) => value as any,
    });

export declare namespace CreateProblemResponse {
    type Raw = CreateProblemResponse.Success | CreateProblemResponse.Error;

    interface Success {
        type: "success";
        value: serializers.ProblemId.Raw;
    }

    interface Error {
        type: "error";
        value: serializers.CreateProblemError.Raw;
    }
}
