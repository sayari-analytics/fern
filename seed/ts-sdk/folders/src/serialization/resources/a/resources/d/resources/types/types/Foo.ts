/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../../..";
import * as SeedApi from "../../../../../../../../api";
import * as core from "../../../../../../../../core";

export const Foo: core.serialization.Schema<serializers.a.d.Foo.Raw, SeedApi.a.d.Foo> = core.serialization.string();

export declare namespace Foo {
    type Raw = string;
}
