/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../../../../../../..";

export interface TestCaseV2 {
    metadata: SeedTrace.v2.v3.TestCaseMetadata;
    implementation: SeedTrace.v2.v3.TestCaseImplementationReference;
    arguments: Record<SeedTrace.v2.v3.ParameterId, SeedTrace.VariableValue>;
    expects?: SeedTrace.v2.v3.TestCaseExpects;
}
