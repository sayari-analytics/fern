import { AbsoluteFilePath, join } from "@fern-api/core-utils";
import { getViolationsForRule } from "../../../testing-utils/getViolationsForRule";
import { ValidationViolation } from "../../../ValidationViolation";
import { NoObjectSinglePropertyKeyRule } from "../no-object-single-property-key";

describe("valid-field-names", () => {
    it("simple", async () => {
        const violations = await getViolationsForRule({
            rule: NoObjectSinglePropertyKeyRule,
            absolutePathToWorkspace: join(AbsoluteFilePath.of(__dirname), "fixtures", "simple"),
        });

        const expectedViolations: ValidationViolation[] = [
            {
                message: "Union subtype d extends an object, so key cannot be defined",
                nodePath: ["types", "MyUnion"],
                relativeFilepath: "posts.yml",
                severity: "error",
            },
            {
                message: "Union subtype e has no body, so key cannot be defined",
                nodePath: ["types", "MyUnion"],
                relativeFilepath: "posts.yml",
                severity: "error",
            },
            {
                message: "Union subtype f has no body, so key cannot be defined",
                nodePath: ["types", "MyUnion"],
                relativeFilepath: "posts.yml",
                severity: "error",
            },
        ];

        expect(violations).toEqual(expectedViolations);
    });
});