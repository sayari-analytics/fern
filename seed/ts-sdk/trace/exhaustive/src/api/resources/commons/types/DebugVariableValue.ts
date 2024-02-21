/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../../..";

export type DebugVariableValue =
    | SeedTrace.DebugVariableValue.IntegerValue
    | SeedTrace.DebugVariableValue.BooleanValue
    | SeedTrace.DebugVariableValue.DoubleValue
    | SeedTrace.DebugVariableValue.StringValue
    | SeedTrace.DebugVariableValue.CharValue
    | SeedTrace.DebugVariableValue.MapValue
    | SeedTrace.DebugVariableValue.ListValue
    | SeedTrace.DebugVariableValue.BinaryTreeNodeValue
    | SeedTrace.DebugVariableValue.SinglyLinkedListNodeValue
    | SeedTrace.DebugVariableValue.DoublyLinkedListNodeValue
    | SeedTrace.DebugVariableValue.UndefinedValue
    | SeedTrace.DebugVariableValue.NullValue
    | SeedTrace.DebugVariableValue.GenericValue
    | SeedTrace.DebugVariableValue._Unknown;

export declare namespace DebugVariableValue {
    interface IntegerValue extends _Utils {
        type: "integerValue";
        value: number;
    }

    interface BooleanValue extends _Utils {
        type: "booleanValue";
        value: boolean;
    }

    interface DoubleValue extends _Utils {
        type: "doubleValue";
        value: number;
    }

    interface StringValue extends _Utils {
        type: "stringValue";
        value: string;
    }

    interface CharValue extends _Utils {
        type: "charValue";
        value: string;
    }

    interface MapValue extends SeedTrace.DebugMapValue, _Utils {
        type: "mapValue";
    }

    interface ListValue extends _Utils {
        type: "listValue";
        value: SeedTrace.DebugVariableValue[];
    }

    interface BinaryTreeNodeValue extends SeedTrace.BinaryTreeNodeAndTreeValue, _Utils {
        type: "binaryTreeNodeValue";
    }

    interface SinglyLinkedListNodeValue extends SeedTrace.SinglyLinkedListNodeAndListValue, _Utils {
        type: "singlyLinkedListNodeValue";
    }

    interface DoublyLinkedListNodeValue extends SeedTrace.DoublyLinkedListNodeAndListValue, _Utils {
        type: "doublyLinkedListNodeValue";
    }

    interface UndefinedValue extends _Utils {
        type: "undefinedValue";
    }

    interface NullValue extends _Utils {
        type: "nullValue";
    }

    interface GenericValue extends SeedTrace.GenericValue, _Utils {
        type: "genericValue";
    }

    interface _Unknown extends _Utils {
        type: void;
    }

    interface _Utils {
        _visit: <_Result>(visitor: SeedTrace.DebugVariableValue._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        integerValue: (value: number) => _Result;
        booleanValue: (value: boolean) => _Result;
        doubleValue: (value: number) => _Result;
        stringValue: (value: string) => _Result;
        charValue: (value: string) => _Result;
        mapValue: (value: SeedTrace.DebugMapValue) => _Result;
        listValue: (value: SeedTrace.DebugVariableValue[]) => _Result;
        binaryTreeNodeValue: (value: SeedTrace.BinaryTreeNodeAndTreeValue) => _Result;
        singlyLinkedListNodeValue: (value: SeedTrace.SinglyLinkedListNodeAndListValue) => _Result;
        doublyLinkedListNodeValue: (value: SeedTrace.DoublyLinkedListNodeAndListValue) => _Result;
        undefinedValue: () => _Result;
        nullValue: () => _Result;
        genericValue: (value: SeedTrace.GenericValue) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const DebugVariableValue = {
    integerValue: (value: number): SeedTrace.DebugVariableValue.IntegerValue => {
        return {
            value: value,
            type: "integerValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.IntegerValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    booleanValue: (value: boolean): SeedTrace.DebugVariableValue.BooleanValue => {
        return {
            value: value,
            type: "booleanValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.BooleanValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    doubleValue: (value: number): SeedTrace.DebugVariableValue.DoubleValue => {
        return {
            value: value,
            type: "doubleValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.DoubleValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    stringValue: (value: string): SeedTrace.DebugVariableValue.StringValue => {
        return {
            value: value,
            type: "stringValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.StringValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    charValue: (value: string): SeedTrace.DebugVariableValue.CharValue => {
        return {
            value: value,
            type: "charValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.CharValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    mapValue: (value: SeedTrace.DebugMapValue): SeedTrace.DebugVariableValue.MapValue => {
        return {
            ...value,
            type: "mapValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.MapValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    listValue: (value: SeedTrace.DebugVariableValue[]): SeedTrace.DebugVariableValue.ListValue => {
        return {
            value: value,
            type: "listValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.ListValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    binaryTreeNodeValue: (
        value: SeedTrace.BinaryTreeNodeAndTreeValue
    ): SeedTrace.DebugVariableValue.BinaryTreeNodeValue => {
        return {
            ...value,
            type: "binaryTreeNodeValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.BinaryTreeNodeValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    singlyLinkedListNodeValue: (
        value: SeedTrace.SinglyLinkedListNodeAndListValue
    ): SeedTrace.DebugVariableValue.SinglyLinkedListNodeValue => {
        return {
            ...value,
            type: "singlyLinkedListNodeValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.SinglyLinkedListNodeValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    doublyLinkedListNodeValue: (
        value: SeedTrace.DoublyLinkedListNodeAndListValue
    ): SeedTrace.DebugVariableValue.DoublyLinkedListNodeValue => {
        return {
            ...value,
            type: "doublyLinkedListNodeValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.DoublyLinkedListNodeValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    undefinedValue: (): SeedTrace.DebugVariableValue.UndefinedValue => {
        return {
            type: "undefinedValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.UndefinedValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    nullValue: (): SeedTrace.DebugVariableValue.NullValue => {
        return {
            type: "nullValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.NullValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    genericValue: (value: SeedTrace.GenericValue): SeedTrace.DebugVariableValue.GenericValue => {
        return {
            ...value,
            type: "genericValue",
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue.GenericValue,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    _unknown: (value: { type: string }): SeedTrace.DebugVariableValue._Unknown => {
        return {
            ...(value as any),
            _visit: function <_Result>(
                this: SeedTrace.DebugVariableValue._Unknown,
                visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
            ) {
                return SeedTrace.DebugVariableValue._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(
        value: SeedTrace.DebugVariableValue,
        visitor: SeedTrace.DebugVariableValue._Visitor<_Result>
    ): _Result => {
        switch (value.type) {
            case "integerValue":
                return visitor.integerValue(value.value);
            case "booleanValue":
                return visitor.booleanValue(value.value);
            case "doubleValue":
                return visitor.doubleValue(value.value);
            case "stringValue":
                return visitor.stringValue(value.value);
            case "charValue":
                return visitor.charValue(value.value);
            case "mapValue":
                return visitor.mapValue(value);
            case "listValue":
                return visitor.listValue(value.value);
            case "binaryTreeNodeValue":
                return visitor.binaryTreeNodeValue(value);
            case "singlyLinkedListNodeValue":
                return visitor.singlyLinkedListNodeValue(value);
            case "doublyLinkedListNodeValue":
                return visitor.doublyLinkedListNodeValue(value);
            case "undefinedValue":
                return visitor.undefinedValue();
            case "nullValue":
                return visitor.nullValue();
            case "genericValue":
                return visitor.genericValue(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;
