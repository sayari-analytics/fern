/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";
export declare const TestCaseResultWithStdout: core.serialization.ObjectSchema<serializers.TestCaseResultWithStdout.Raw, SeedTrace.TestCaseResultWithStdout>;
export declare namespace TestCaseResultWithStdout {
    interface Raw {
        result: serializers.TestCaseResult.Raw;
        stdout: string;
    }
}
