/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as errors from "../../../../errors";

export class BadRequest extends errors.SeedCustomAuthError {
    constructor() {
        super({
            message: "BadRequest",
            statusCode: 400,
        });
        Object.setPrototypeOf(this, BadRequest.prototype);
    }
}
