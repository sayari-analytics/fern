// Generated by Fern. Do not edit.

package api

import (
	context "context"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/path-params/fixtures/core"
)

type Service interface {
	GetUser(ctx context.Context, userId string) (string, error)
	GetUserV2(ctx context.Context, userId string) (string, error)
	GetUserV3(ctx context.Context, userId string, infoId string) (string, error)
}

func NewClient(baseURL string, httpClient core.HTTPClient, opts ...core.ClientOption) (Service, error) {
	options := new(core.ClientOptions)
	for _, opt := range opts {
		opt(options)
	}
	return &client{
		getUserEndpoint:   newGetUserEndpoint(baseURL, httpClient, options),
		getUserV2Endpoint: newGetUserV2Endpoint(baseURL, httpClient, options),
		getUserV3Endpoint: newGetUserV3Endpoint(baseURL, httpClient, options),
	}, nil
}

type client struct {
	getUserEndpoint   *getUserEndpoint
	getUserV2Endpoint *getUserV2Endpoint
	getUserV3Endpoint *getUserV3Endpoint
}

func (g *client) GetUser(ctx context.Context, userId string) (string, error) {
	return g.getUserEndpoint.Call(ctx, userId)
}

func (g *client) GetUserV2(ctx context.Context, userId string) (string, error) {
	return g.getUserV2Endpoint.Call(ctx, userId)
}

func (g *client) GetUserV3(ctx context.Context, userId string, infoId string) (string, error) {
	return g.getUserV3Endpoint.Call(ctx, userId, infoId)
}
