// This file was auto-generated by Fern from our API Definition.

package api

type GetAllUsersRequest struct {
	XEndpointHeader string `json:"-" url:"-"`
	Limit           *int   `json:"-" url:"limit,omitempty"`
	key             string
}

func (g *GetAllUsersRequest) Key() string {
	return g.key
}
