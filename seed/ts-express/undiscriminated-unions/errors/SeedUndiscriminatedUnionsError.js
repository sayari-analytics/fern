"use strict";
/**
 * This file was auto-generated by Fern from our API Definition.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.SeedUndiscriminatedUnionsError = void 0;
class SeedUndiscriminatedUnionsError extends Error {
    constructor(errorName) {
        super();
        this.errorName = errorName;
        Object.setPrototypeOf(this, SeedUndiscriminatedUnionsError.prototype);
    }
}
exports.SeedUndiscriminatedUnionsError = SeedUndiscriminatedUnionsError;
