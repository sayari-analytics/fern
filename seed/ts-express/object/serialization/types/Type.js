"use strict";
/**
 * This file was auto-generated by Fern from our API Definition.
 */
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Type = void 0;
const core = __importStar(require("../../core"));
exports.Type = core.serialization.object({
    one: core.serialization.number(),
    two: core.serialization.number(),
    three: core.serialization.string(),
    four: core.serialization.boolean(),
    five: core.serialization.number(),
    six: core.serialization.date(),
    seven: core.serialization.string(),
    eight: core.serialization.string(),
    nine: core.serialization.string(),
    ten: core.serialization.list(core.serialization.number()),
    eleven: core.serialization.set(core.serialization.number()),
    twelve: core.serialization.record(core.serialization.string(), core.serialization.boolean()),
    thirteen: core.serialization.number().optional(),
    fourteen: core.serialization.unknown(),
    fifteen: core.serialization.list(core.serialization.list(core.serialization.number())),
    sixteen: core.serialization.list(core.serialization.record(core.serialization.string(), core.serialization.number())),
    seventeen: core.serialization.list(core.serialization.string().optional()),
    eighteen: core.serialization.stringLiteral("eighteen"),
    nineteen: core.serialization.lazyObject(() => __awaiter(void 0, void 0, void 0, function* () { return (yield Promise.resolve().then(() => __importStar(require("..")))).Name; })),
});
