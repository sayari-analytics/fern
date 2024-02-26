/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const DateWithExample: core.serialization.ObjectSchema<
    serializers.DateWithExample.Raw,
    FernOpenapiIr.DateWithExample
> = core.serialization.objectWithoutOptionalProperties({
    example: core.serialization.string().optional(),
});

export declare namespace DateWithExample {
    interface Raw {
        example?: string | null;
    }
}
