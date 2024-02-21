/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";
export declare const UnexpectedLanguageError: core.serialization.ObjectSchema<serializers.UnexpectedLanguageError.Raw, SeedTrace.UnexpectedLanguageError>;
export declare namespace UnexpectedLanguageError {
    interface Raw {
        expectedLanguage: serializers.Language.Raw;
        actualLanguage: serializers.Language.Raw;
    }
}
