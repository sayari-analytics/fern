/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../..";
import * as SeedEnum from "../../../../../api";
import * as core from "../../../../../core";
export declare const SendEnumInlinedRequest: core.serialization.Schema<serializers.SendEnumInlinedRequest.Raw, SeedEnum.SendEnumInlinedRequest>;
export declare namespace SendEnumInlinedRequest {
    interface Raw {
        operand: serializers.Operand.Raw;
        maybeOperand?: serializers.Operand.Raw | null;
        operandOrColor: serializers.ColorOrOperand.Raw;
        maybeOperandOrColor?: serializers.ColorOrOperand.Raw | null;
    }
}
