/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";

export const InvalidRequestCause: core.serialization.Schema<
    serializers.InvalidRequestCause.Raw,
    SeedTrace.InvalidRequestCause
> = core.serialization
    .union("type", {
        submissionIdNotFound: core.serialization.lazyObject(
            async () => (await import("../../..")).SubmissionIdNotFound
        ),
        customTestCasesUnsupported: core.serialization.lazyObject(
            async () => (await import("../../..")).CustomTestCasesUnsupported
        ),
        unexpectedLanguage: core.serialization.lazyObject(
            async () => (await import("../../..")).UnexpectedLanguageError
        ),
    })
    .transform<SeedTrace.InvalidRequestCause>({
        transform: (value) => value,
        untransform: (value) => value,
    });

export declare namespace InvalidRequestCause {
    type Raw =
        | InvalidRequestCause.SubmissionIdNotFound
        | InvalidRequestCause.CustomTestCasesUnsupported
        | InvalidRequestCause.UnexpectedLanguage;

    interface SubmissionIdNotFound extends serializers.SubmissionIdNotFound.Raw {
        type: "submissionIdNotFound";
    }

    interface CustomTestCasesUnsupported extends serializers.CustomTestCasesUnsupported.Raw {
        type: "customTestCasesUnsupported";
    }

    interface UnexpectedLanguage extends serializers.UnexpectedLanguageError.Raw {
        type: "unexpectedLanguage";
    }
}
