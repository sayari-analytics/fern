/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as SeedTrace from "../../..";
export declare type SubmissionStatusV2 = SeedTrace.SubmissionStatusV2.Test | SeedTrace.SubmissionStatusV2.Workspace;
export declare namespace SubmissionStatusV2 {
    interface Test extends SeedTrace.TestSubmissionStatusV2 {
        type: "test";
    }
    interface Workspace extends SeedTrace.WorkspaceSubmissionStatusV2 {
        type: "workspace";
    }
}
