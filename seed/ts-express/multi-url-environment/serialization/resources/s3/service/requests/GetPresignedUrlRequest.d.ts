/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../..";
import * as SeedMultiUrlEnvironment from "../../../../../api";
import * as core from "../../../../../core";
export declare const GetPresignedUrlRequest: core.serialization.Schema<serializers.GetPresignedUrlRequest.Raw, SeedMultiUrlEnvironment.GetPresignedUrlRequest>;
export declare namespace GetPresignedUrlRequest {
    interface Raw {
        s3Key: string;
    }
}
