/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../..";
import * as SeedTrace from "../../../../../../api";
import * as core from "../../../../../../core";

export const BasicTestCaseTemplate: core.serialization.ObjectSchema<
    serializers.v2.BasicTestCaseTemplate.Raw,
    SeedTrace.v2.BasicTestCaseTemplate
> = core.serialization.object({
    templateId: core.serialization.lazy(async () => (await import("../../../../..")).v2.TestCaseTemplateId),
    name: core.serialization.string(),
    description: core.serialization.lazyObject(
        async () => (await import("../../../../..")).v2.TestCaseImplementationDescription
    ),
    expectedValueParameterId: core.serialization.lazy(async () => (await import("../../../../..")).v2.ParameterId),
});

export declare namespace BasicTestCaseTemplate {
    interface Raw {
        templateId: serializers.v2.TestCaseTemplateId.Raw;
        name: string;
        description: serializers.v2.TestCaseImplementationDescription.Raw;
        expectedValueParameterId: serializers.v2.ParameterId.Raw;
    }
}
