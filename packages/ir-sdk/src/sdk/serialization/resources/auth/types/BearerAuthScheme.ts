/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const BearerAuthScheme: core.serialization.ObjectSchema<
    serializers.BearerAuthScheme.Raw,
    FernIr.BearerAuthScheme
> = core.serialization
    .objectWithoutOptionalProperties({
        token: core.serialization.lazyObject(async () => (await import("../../..")).Name),
        tokenEnvVar: core.serialization.lazy(async () => (await import("../../..")).EnvironmentVariable).optional(),
    })
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithDocs));

export declare namespace BearerAuthScheme {
    interface Raw extends serializers.WithDocs.Raw {
        token: serializers.Name.Raw;
        tokenEnvVar?: serializers.EnvironmentVariable.Raw | null;
    }
}