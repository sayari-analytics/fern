// This file was auto-generated by Fern from our API Definition.

package user

import (
	json "encoding/json"
	fmt "fmt"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/cycle/fixtures/core"
)

type Username struct {
	Value string `json:"value" url:"value"`

	_rawJSON json.RawMessage
}

func (u *Username) UnmarshalJSON(data []byte) error {
	type unmarshaler Username
	var value unmarshaler
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	*u = Username(value)
	u._rawJSON = json.RawMessage(data)
	return nil
}

func (u *Username) String() string {
	if len(u._rawJSON) > 0 {
		if value, err := core.StringifyJSON(u._rawJSON); err == nil {
			return value
		}
	}
	if value, err := core.StringifyJSON(u); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", u)
}
