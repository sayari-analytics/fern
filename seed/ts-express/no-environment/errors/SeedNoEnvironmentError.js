"use strict";
/**
 * This file was auto-generated by Fern from our API Definition.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.SeedNoEnvironmentError = void 0;
class SeedNoEnvironmentError extends Error {
    constructor(errorName) {
        super();
        this.errorName = errorName;
        Object.setPrototypeOf(this, SeedNoEnvironmentError.prototype);
    }
}
exports.SeedNoEnvironmentError = SeedNoEnvironmentError;
