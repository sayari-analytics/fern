/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";
export declare const MapValue: core.serialization.ObjectSchema<serializers.MapValue.Raw, SeedTrace.MapValue>;
export declare namespace MapValue {
    interface Raw {
        keyValuePairs: serializers.KeyValuePair.Raw[];
    }
}
