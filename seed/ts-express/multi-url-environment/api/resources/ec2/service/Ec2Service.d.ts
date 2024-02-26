/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as SeedMultiUrlEnvironment from "../../..";
import express from "express";
export interface Ec2ServiceMethods {
    bootInstance(req: express.Request<never, never, SeedMultiUrlEnvironment.BootInstanceRequest, never>, res: {
        send: () => Promise<void>;
        cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
        locals: any;
    }): void | Promise<void>;
}
export declare class Ec2Service {
    private readonly methods;
    private router;
    constructor(methods: Ec2ServiceMethods, middleware?: express.RequestHandler[]);
    addMiddleware(handler: express.RequestHandler): this;
    toRouter(): express.Router;
}