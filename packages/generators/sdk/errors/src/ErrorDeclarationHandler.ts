import { ErrorDeclaration } from "@fern-fern/ir-model/errors";
import { ObjectTypeDeclaration } from "@fern-fern/ir-model/types";
import { SdkDeclarationHandler, SdkFile } from "@fern-typescript/sdk-declaration-handler";
import { generateObjectType } from "@fern-typescript/types-v2";
import { ts } from "ts-morph";

export const ErrorDeclarationHandler: SdkDeclarationHandler<ErrorDeclaration> = {
    run: async (errorDeclaration, { file }) => {
        generateObjectType({
            typeName: file.sourceFile.getBaseNameWithoutExtension(),
            docs: errorDeclaration.docs,
            file,
            shape: getErrorShapeWithoutAdditionalProperties(errorDeclaration, file),
            additionalProperties: {
                [file.fernConstants.errorDiscriminant]: ts.factory.createLiteralTypeNode(
                    ts.factory.createStringLiteral(errorDeclaration.discriminantValue.wireValue)
                ),
            },
        });
    },
};

function getErrorShapeWithoutAdditionalProperties(
    errorDeclaration: ErrorDeclaration,
    file: SdkFile
): ObjectTypeDeclaration {
    if (errorDeclaration.type._type === "alias") {
        const resolvedType = file.resolveTypeReference(errorDeclaration.type.aliasOf);
        if (resolvedType._type === "void") {
            return { extends: [], properties: [] };
        }
    }

    if (errorDeclaration.type._type === "object") {
        return errorDeclaration.type;
    }

    throw new Error("Error declaration type must be an object");
}
