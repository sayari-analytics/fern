package api

import (
	json "encoding/json"
	fmt "fmt"
)

type Union struct {
	Type        string
	FooAlias    *Foo
	BarAlias    BarAlias
	DoubleAlias Double
}

func (x *Union) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	x.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "fooAlias":
		value := new(Foo)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		x.FooAlias = value
	case "barAlias":
		var valueUnmarshaler struct {
			BarAlias BarAlias `json:"barAlias"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		x.BarAlias = valueUnmarshaler.BarAlias
	case "doubleAlias":
		var valueUnmarshaler struct {
			DoubleAlias Double `json:"doubleAlias"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		x.DoubleAlias = valueUnmarshaler.DoubleAlias
	}
	return nil
}

type UnionVisitor interface {
	VisitFooAlias(*Foo) error
	VisitBarAlias(BarAlias) error
	VisitDoubleAlias(Double) error
}

func (x *Union) Accept(v UnionVisitor) error {
	switch x.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", x.Type, x)
	case "fooAlias":
		return v.VisitFooAlias(x.FooAlias)
	case "barAlias":
		return v.VisitBarAlias(x.BarAlias)
	case "doubleAlias":
		return v.VisitDoubleAlias(x.DoubleAlias)
	}
}
