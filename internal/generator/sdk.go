package generator

import (
	_ "embed"
	"errors"
	"fmt"
	"path"
	"strings"

	"github.com/fern-api/fern-go/internal/fern/ir"
)

//go:embed sdk/core/core.go
var coreFile string

// WriteCore writes the core utilities required by the generated
// service code. This includes the ClientOption type, auth options,
// and HTTPClient interface declaration.
func (f *fileWriter) WriteCoreClientOptions(auth *ir.ApiAuth) error {
	importPath := path.Join(f.baseImportPath, "core")

	// We have at least one auth scheme, so we need to generate the ClientOption.
	f.P("type ClientOption func(*ClientOptions)")
	f.P()

	if auth == nil || len(auth.Schemes) == 0 {
		// We don't have any auth options to write, but we still generate
		// the ClientOptions structure for the endpoints to act upon.
		f.P("type ClientOptions struct {}")
		f.P()

		f.P("func (c *ClientOptions) ToHeader() http.Header { return nil }")
		f.P()
		return nil
	}

	// Generate the exported ClientOptions type that all clients can act upon.
	f.P("type ClientOptions struct {")
	for _, authScheme := range auth.Schemes {
		if authScheme.Bearer != nil {
			f.P("Bearer string")
		}
		if authScheme.Basic != nil {
			f.P("Username string")
			f.P("Password string")
		}
		if authScheme.Header != nil {
			f.P(
				authScheme.Header.Name.Name.PascalCase.UnsafeName,
				" ",
				typeReferenceToGoType(authScheme.Header.ValueType, f.types, f.imports, f.baseImportPath, importPath),
			)
		}
	}
	f.P("}")
	f.P()

	// Generat the authorization functional options.
	for _, authScheme := range auth.Schemes {
		if authScheme.Bearer != nil {
			f.P("func ClientWithAuthBearer(bearer string) ClientOption {")
			f.P("return func(opts *ClientOptions) {")
			f.P("opts.Bearer = bearer")
			f.P("}")
			f.P("}")
			f.P()
		}
		if authScheme.Basic != nil {
			f.P("func ClientWithAuthBasic(username, password string) ClientOption {")
			f.P("return func(opts *ClientOptions) {")
			f.P("opts.Username = username")
			f.P("opts.Password = password")
			f.P("}")
			f.P("}")
			f.P()
		}
		if authScheme.Header != nil {
			var (
				optionName = fmt.Sprintf("ClientWithAuth%s", authScheme.Header.Name.Name.PascalCase.UnsafeName)
				field      = authScheme.Header.Name.Name.PascalCase.UnsafeName
				param      = authScheme.Header.Name.Name.CamelCase.SafeName
				value      = typeReferenceToGoType(authScheme.Header.ValueType, f.types, f.imports, f.baseImportPath, importPath)
			)
			f.P("func ", optionName, "(", param, " ", value, ") ClientOption {")
			f.P("return func(opts *ClientOptions) {")
			f.P("opts.", field, " = ", param)
			f.P("}")
			f.P("}")
			f.P()
		}
	}

	// Generate the ToHeader method.
	f.P("func (c *ClientOptions) ToHeader() http.Header {")
	f.P("header := make(http.Header)")
	for _, authScheme := range auth.Schemes {
		if authScheme.Bearer != nil {
			f.P(`if c.Bearer != "" { `)
			f.P(`header.Set("Authorization", `, `"Bearer " + c.Bearer)`)
			f.P("}")
		}
		if authScheme.Basic != nil {
			f.P(`if c.Username != "" && c.Password != "" {`)
			f.P(`header.Set("Authorization", `, `"Basic " + base64.StdEncoding.EncodeToString([]byte(c.Username + ": " + c.Password)))`)
			f.P("}")
		}
		if header := authScheme.Header; header != nil {
			var prefix string
			if header.Prefix != nil {
				prefix = *header.Prefix + " "
			}
			f.P("var value ", typeReferenceToGoType(authScheme.Header.ValueType, f.types, f.imports, f.baseImportPath, importPath))
			f.P("if c.", header.Name.Name.PascalCase.UnsafeName, " != value {")
			f.P(`header.Set("`, header.Name.WireValue, `", fmt.Sprintf("`, prefix, `%v", c.`, header.Name.Name.PascalCase.UnsafeName, "))")
			f.P("}")
		}
	}
	f.P("return header")
	f.P("}")
	f.P()

	return nil
}

// WriteClient writes a client for interacting with the given service.
func (f *fileWriter) WriteClient(irEndpoints []*ir.HttpEndpoint, subpackages []*ir.Subpackage, fernFilepath *ir.FernFilepath, namePrefix *ir.Name) error {
	var (
		clientName     = "Client"
		clientImplName = "client"
		receiver       = "c"
	)
	if namePrefix != nil {
		clientImplName = namePrefix.CamelCase.UnsafeName + clientName
		clientName = namePrefix.PascalCase.UnsafeName + clientName
		receiver = typeNameToReceiver(clientImplName)
	}
	// Reformat the endpoint data into a structure that's suitable for code generation.
	var endpoints []*endpoint
	for _, irEndpoint := range irEndpoints {
		endpoint, err := f.endpointFromIR(fernFilepath, irEndpoint, receiver)
		if err != nil {
			return err
		}
		endpoints = append(endpoints, endpoint)
	}
	// Generate the service interface definition.
	f.P("type ", clientName, " interface {")
	for _, endpoint := range endpoints {
		f.P(fmt.Sprintf("%s(%s) %s", endpoint.Name.PascalCase.UnsafeName, endpoint.SignatureParameters, endpoint.ReturnValues))
	}
	for _, subpackage := range subpackages {
		// Define a getter method for the subpackage client.
		//
		// If this is a top-level client (i.e. defined by a __package__.yml),
		// it will have getters for each of the files in the same package.
		//
		//  type Client interface {
		//    User() UserClient
		//    Notification() NotificationClient
		//  }
		//
		// TODO: Temporary solution - refactor this conditional when the IR is updated.
		if subpackage.FernFilepath.File != nil {
			clientTypeName := subpackage.FernFilepath.File.PascalCase.UnsafeName + "Client"
			f.P(subpackage.Name.PascalCase.UnsafeName, "()", clientTypeName)
			continue
		}
		var (
			importPath     = fernFilepathToImportPath(f.baseImportPath, subpackage.FernFilepath)
			clientTypeName = f.imports.Add(importPath) + ".Client"
		)
		f.P(subpackage.Name.PascalCase.UnsafeName, "()", clientTypeName)
	}
	f.P("}")
	f.P()

	// Generate the client constructor.
	f.P("func New", clientName, "(baseURL string, httpClient core.HTTPClient, opts ...core.ClientOption) ", clientName, " {")
	f.P("options := new(core.ClientOptions)")
	f.P("for _, opt := range opts {")
	f.P("opt(options)")
	f.P("}")
	f.P("return &", clientImplName, "{")
	f.P(`baseURL: strings.TrimRight(baseURL, "/"),`)
	f.P("httpClient: httpClient,")
	f.P("header: options.ToHeader(),")
	for _, subpackage := range subpackages {
		// TODO: Temporary solution - refactor this conditional when the IR is updated.
		if subpackage.FernFilepath.File != nil {
			clientTypeName := subpackage.FernFilepath.File.PascalCase.UnsafeName + "Client"
			clientConstructor := "New" + clientTypeName + "(baseURL, httpClient, opts...),"
			f.P(subpackage.Name.CamelCase.UnsafeName, "Client: ", clientConstructor)
			continue
		}
		var (
			importPath        = fernFilepathToImportPath(f.baseImportPath, subpackage.FernFilepath)
			clientConstructor = f.imports.Add(importPath) + ".NewClient(baseURL, httpClient, opts...),"
		)
		f.P(subpackage.Name.CamelCase.UnsafeName, "Client: ", clientConstructor)
	}
	f.P("}")
	f.P("}")
	f.P()

	// Generate the client implementation.
	f.P("type ", clientImplName, " struct {")
	f.P("baseURL string")
	f.P("httpClient core.HTTPClient")
	f.P("header http.Header")
	for _, subpackage := range subpackages {
		// TODO: Temporary solution - refactor this conditional when the IR is updated.
		var (
			importPath     = fernFilepathToImportPath(f.baseImportPath, subpackage.FernFilepath)
			clientTypeName = f.imports.Add(importPath) + "." + clientName
		)
		if subpackage.FernFilepath.File != nil {
			clientTypeName = subpackage.FernFilepath.File.PascalCase.UnsafeName + "Client"
		}
		f.P(subpackage.Name.CamelCase.UnsafeName, "Client ", clientTypeName)
	}
	f.P("}")
	f.P()

	// Implement this service's methods.
	for _, endpoint := range endpoints {
		f.P("func (", receiver, " *", clientImplName, ") ", endpoint.Name.PascalCase.UnsafeName, "(", endpoint.SignatureParameters, ") ", endpoint.ReturnValues, " {")
		if len(endpoint.Errors) > 0 {
			f.P("errorDecoder := func(statusCode int, body io.Reader) error {")
			f.P("raw, err := io.ReadAll(body)")
			f.P("if err != nil {")
			f.P("return err")
			f.P("}")
			f.P("apiError := core.NewAPIError(statusCode, errors.New(string(raw)))")
			f.P("decoder := json.NewDecoder(bytes.NewReader(raw))")
			f.P("switch statusCode {")
			for _, responseError := range endpoint.Errors {
				errorDeclaration := f.errors[responseError.Error.ErrorId]
				f.P("case ", errorDeclaration.StatusCode, ":")
				f.P("value := new(", errorDeclaration.Name.Name.PascalCase.UnsafeName, ")")
				f.P("if err := decoder.Decode(value); err != nil {")
				f.P("return err")
				f.P("}")
				f.P("value.APIError = apiError")
				f.P("return value")
			}
			// Close the switch statement.
			f.P("}")
			f.P("return apiError")
			f.P("}")
			f.P()
		}
		// Add endpoint-specific headers from the request, if any.
		f.P("headers := ", receiver, ".header.Clone()")
		if len(endpoint.Headers) > 0 {
			for _, header := range endpoint.Headers {
				headerType := typeReferenceToGoType(header.ValueType, f.types, f.imports, f.baseImportPath, endpoint.ImportPath)
				requestField := endpoint.RequestParameterName + "." + header.Name.Name.PascalCase.UnsafeName
				if header.ValueType.Container != nil && header.ValueType.Container.Optional != nil {
					requestField = fmt.Sprintf("*%s", requestField)
				}
				f.P("var ", header.Name.Name.CamelCase.SafeName, "DefaultValue ", headerType)
				f.P("if ", endpoint.RequestParameterName, ".", header.Name.Name.PascalCase.UnsafeName, "!= ", header.Name.Name.CamelCase.SafeName, "DefaultValue {")
				f.P(`headers.Add("`, header.Name.WireValue, `", fmt.Sprintf("%v", `, requestField, "))")
				f.P("}")
			}
			f.P()
		}
		// Compose the URL, including any query parameters.
		f.P(endpoint.URLStatement)
		if len(endpoint.QueryParameters) > 0 {
			f.P("queryParams := make(url.Values)")
			for _, queryParameter := range endpoint.QueryParameters {
				queryParameterType := typeReferenceToGoType(queryParameter.ValueType, f.types, f.imports, f.baseImportPath, endpoint.ImportPath)
				if queryParameter.AllowMultiple {
					requestField := "value"
					if queryParameter.ValueType.Container != nil && queryParameter.ValueType.Container.Optional != nil {
						// TODO: For now, we recognize whether or not we need to dereference the query parameter based on whether or not it's an optional.
						// As long as Fern supports them, we should support all different types of complex query parameter structures. To avoid complexity
						// in the generated code, we might want to use a reflect-based approach.
						requestField = fmt.Sprintf("*%s", requestField)
					}
					f.P("for _, value := range ", endpoint.RequestParameterName, ".", queryParameter.Name.Name.PascalCase.UnsafeName, "{")
					f.P(`queryParams.Add("`, queryParameter.Name.WireValue, `", fmt.Sprintf("%v", `, requestField, "))")
					f.P("}")
				} else {
					requestField := endpoint.RequestParameterName + "." + queryParameter.Name.Name.PascalCase.UnsafeName
					if queryParameter.ValueType.Container != nil && queryParameter.ValueType.Container.Optional != nil {
						// TODO: For now, we recognize whether or not we need to dereference the query parameter based on whether or not it's an optional.
						// As long as Fern supports them, we should support all different types of complex query parameter structures. To avoid complexity
						// in the generated code, we might want to use a reflect-based approach.
						requestField = fmt.Sprintf("*%s", requestField)
					}
					f.P("var ", queryParameter.Name.Name.CamelCase.SafeName, "DefaultValue ", queryParameterType)
					f.P("if ", endpoint.RequestParameterName, ".", queryParameter.Name.Name.PascalCase.UnsafeName, "!= ", queryParameter.Name.Name.CamelCase.SafeName, "DefaultValue {")
					f.P(`queryParams.Add("`, queryParameter.Name.WireValue, `", fmt.Sprintf("%v", `, requestField, "))")
					f.P("}")
				}
			}
			f.P("if len(queryParams) > 0 {")
			f.P(`endpointURL += "?" + queryParams.Encode()`)
			f.P("}")
			f.P()
		}
		// Prepare a response variable and issue the request.
		if endpoint.ResponseType != "" {
			f.P(fmt.Sprintf(endpoint.ResponseInitializerFormat, strings.TrimLeft(endpoint.ResponseType, "*")))
		}
		f.P("if err := core.DoRequest(")
		f.P("ctx,")
		f.P(receiver, ".httpClient,")
		f.P("endpointURL, ")
		f.P(endpoint.Method, ",")
		f.P(endpoint.RequestParameterName, ",")
		f.P(endpoint.ResponseParameterName, ",")
		f.P("headers,")
		f.P(endpoint.ErrorDecoderParameterName, ",")
		f.P("); err != nil {")
		f.P("return ", endpoint.ErrorReturnValues)
		f.P("}")
		f.P("return ", endpoint.SuccessfulReturnValues)
		f.P("}")
		f.P()
	}

	// Implement the getter methods to nested clients, if any.
	for _, subpackage := range subpackages {
		// TODO: Temporary solution - refactor this conditional when the IR is updated.
		var (
			importPath     = fernFilepathToImportPath(f.baseImportPath, subpackage.FernFilepath)
			clientTypeName = f.imports.Add(importPath) + ".Client"
		)
		if subpackage.FernFilepath.File != nil {
			clientTypeName = subpackage.FernFilepath.File.PascalCase.UnsafeName + "Client"
		}
		f.P("func (", receiver, " *", clientImplName, ") ", subpackage.Name.PascalCase.UnsafeName, "() ", clientTypeName, " {")
		f.P("return ", receiver, ".", subpackage.Name.CamelCase.UnsafeName, "Client")
		f.P("}")
		f.P()
	}

	return nil
}

// endpoint holds the fields required to generate a client endpoint.
//
// All of the fields are pre-formatted so that they can all be simple
// strings.
type endpoint struct {
	Name                      *ir.Name
	ImportPath                string
	RequestParameterName      string
	ResponseType              string
	ResponseParameterName     string
	ResponseInitializerFormat string
	PathParameterNames        string
	AllParameterNames         string
	SignatureParameters       string
	ReturnValues              string
	SuccessfulReturnValues    string
	ErrorReturnValues         string
	URLStatement              string
	Method                    string
	ErrorDecoderParameterName string
	Errors                    ir.ResponseErrors
	QueryParameters           []*ir.QueryParameter
	Headers                   []*ir.HttpHeader
}

// signatureForEndpoint returns a signature template for the given endpoint.
func (f *fileWriter) endpointFromIR(fernFilepath *ir.FernFilepath, irEndpoint *ir.HttpEndpoint, receiver string) (*endpoint, error) {
	importPath := fernFilepathToImportPath(f.baseImportPath, fernFilepath)

	// Add path parameters and request body, if any.
	signatureParameters := "ctx context.Context"
	var pathParameterNames []string
	for _, pathParameter := range irEndpoint.AllPathParameters {
		pathParameterName := pathParameter.Name.CamelCase.SafeName
		parameterType := typeReferenceToGoType(pathParameter.ValueType, f.types, f.imports, f.baseImportPath, importPath)
		signatureParameters += fmt.Sprintf(", %s %s", pathParameterName, parameterType)
		pathParameterNames = append(pathParameterNames, pathParameterName)
	}

	// Format the rest of the request parameters.
	requestParameterName := "nil"
	if irEndpoint.SdkRequest != nil {
		var requestType string
		if requestBody := irEndpoint.SdkRequest.Shape.JustRequestBody; requestBody != nil {
			requestType = typeReferenceToGoType(requestBody.RequestBodyType, f.types, f.imports, f.baseImportPath, importPath)
		}
		if irEndpoint.SdkRequest.Shape.Wrapper != nil {
			// If this is a wrapper type, it's guaranteed to be generated in the same package,
			// so we don't need to consult its Fern filepath.
			requestType = fmt.Sprintf("*%s", irEndpoint.SdkRequest.Shape.Wrapper.WrapperName.PascalCase.UnsafeName)
		}
		requestParameterName = irEndpoint.SdkRequest.RequestParameterName.CamelCase.SafeName
		signatureParameters += fmt.Sprintf(", %s %s", requestParameterName, requestType)
	}

	// Format the parameter names so that they're suitable for
	// the client method call.
	allParameterNames := append([]string{"ctx"}, pathParameterNames...)
	if requestParameterName != "nil" {
		allParameterNames = append(allParameterNames, requestParameterName)
	}

	// Format all of the response values.
	var (
		responseType              string
		responseParameterName     string
		responseInitializerFormat string
		signatureReturnValues     string
		successfulReturnValues    string
		errorReturnValues         string
	)
	if irEndpoint.Response != nil {
		if irEndpoint.Response.Json == nil {
			return nil, fmt.Errorf("the SDK generator only supports JSON-based responses, but found %q", irEndpoint.Response.Type)
		}
		responseType = typeReferenceToGoType(irEndpoint.Response.Json.ResponseBodyType, f.types, f.imports, f.baseImportPath, importPath)
		responseInitializerFormat = "var response %s"
		if named := irEndpoint.Response.Json.ResponseBodyType.Named; named != nil && isPointer(f.types[named.TypeId]) {
			responseInitializerFormat = "response := new(%s)"
		}
		responseParameterName = "&response"
		signatureReturnValues = fmt.Sprintf("(%s, error)", responseType)
		successfulReturnValues = "response, nil"
		errorReturnValues = "response, err"
	} else {
		responseParameterName = "nil"
		signatureReturnValues = "error"
		successfulReturnValues = "nil"
		errorReturnValues = "err"
	}

	// Consolidate the irEndpoint's full path into a path suffix that
	// can be applied to the irEndpoint at construction time.
	var pathSuffix string
	if irEndpoint.FullPath != nil {
		if irEndpoint.FullPath.Head != "/" {
			pathSuffix = irEndpoint.FullPath.Head
		}
		for _, part := range irEndpoint.FullPath.Parts {
			if part.PathParameter != "" {
				pathSuffix += "%v"
			}
			if part.Tail != "" {
				pathSuffix += part.Tail
			}
		}
	}

	// Determine the URL statement used in the endpoint implementation.
	baseURL := fmt.Sprintf("%s.baseURL", receiver)
	if len(pathSuffix) > 0 {
		baseURL = baseURL + ` + "/" + ` + fmt.Sprintf("%q", pathSuffix)
	}
	urlStatement := fmt.Sprintf("endpointURL := %s", baseURL)
	if len(pathParameterNames) > 0 {
		urlStatement = "endpointURL := fmt.Sprintf(" + baseURL + ", " + strings.Join(pathParameterNames, ", ") + ")"
	}

	// An error decoder is required when there are endpoint-specific errors.
	errorDecoderParameterName := "nil"
	if len(irEndpoint.Errors) > 0 {
		errorDecoderParameterName = "errorDecoder"
	}

	return &endpoint{
		Name:                      irEndpoint.Name,
		ImportPath:                importPath,
		RequestParameterName:      requestParameterName,
		ResponseType:              responseType,
		ResponseParameterName:     responseParameterName,
		ResponseInitializerFormat: responseInitializerFormat,
		PathParameterNames:        strings.Join(pathParameterNames, ", "),
		AllParameterNames:         strings.Join(allParameterNames, ", "),
		SignatureParameters:       signatureParameters,
		ReturnValues:              signatureReturnValues,
		SuccessfulReturnValues:    successfulReturnValues,
		ErrorReturnValues:         errorReturnValues,
		URLStatement:              urlStatement,
		Method:                    irMethodToMethodEnum(irEndpoint.Method),
		ErrorDecoderParameterName: errorDecoderParameterName,
		Errors:                    irEndpoint.Errors,
		QueryParameters:           irEndpoint.QueryParameters,
		Headers:                   irEndpoint.Headers,
	}, nil
}

// WriteError writes the structured error types.
func (f *fileWriter) WriteError(errorDeclaration *ir.ErrorDeclaration) error {
	var (
		typeName   = errorDeclaration.Name.Name.PascalCase.UnsafeName
		receiver   = typeNameToReceiver(typeName)
		importPath = fernFilepathToImportPath(f.baseImportPath, errorDeclaration.Name.FernFilepath)
		value      = typeReferenceToGoType(errorDeclaration.Type, f.types, f.imports, f.baseImportPath, importPath)
	)
	var literal string
	isLiteral := errorDeclaration.Type.Container != nil && errorDeclaration.Type.Container.Literal != nil
	if isLiteral {
		literal = literalToValue(errorDeclaration.Type.Container.Literal)
	}

	// Generate the error type declaration.
	f.P("type ", typeName, " struct {")
	f.P("*core.APIError")
	if errorDeclaration.Type == nil {
		// This error doesn't have a body, so we only need to include the status code.
		f.P("}")
		f.P()
		return nil
	}
	f.P("Body ", value)
	f.P("}")
	f.P()

	// Implement the json.Unmarshaler.
	format := "var body %s"
	if errorDeclaration.Type.Named != nil && isPointer(f.types[errorDeclaration.Type.Named.TypeId]) {
		format = "body := new(%s)"
		value = strings.TrimLeft(value, "*")
	}
	f.P("func (", receiver, "*", typeName, ") UnmarshalJSON(data []byte) error {")
	f.P(fmt.Sprintf(format, value))
	f.P("if err := json.Unmarshal(data, &body); err != nil {")
	f.P("return err")
	f.P("}")
	if isLiteral {
		// If the error specifies a literal, it will only succeed if the literal matches exactly.
		f.P("if body != ", literal, " {")
		f.P(`return fmt.Errorf("expected literal %q, but found %q", `, literal, ", body)")
		f.P("}")
	}
	f.P(receiver, ".StatusCode = ", errorDeclaration.StatusCode)
	f.P(receiver, ".Body = body")
	f.P("return nil")
	f.P("}")
	f.P()

	// Implement the json.Marshaler.
	f.P("func (", receiver, "*", typeName, ") MarshalJSON() ([]byte, error) {")
	if isLiteral {
		f.P("return json.Marshal(", literal, ")")
	} else {
		f.P("return json.Marshal(", receiver, ".Body)")
	}
	f.P("}")
	f.P()
	return nil
}

// WriteRequestType writes a type dedicated to the in-lined request (if any).
func (f *fileWriter) WriteRequestType(fernFilepath *ir.FernFilepath, endpoint *ir.HttpEndpoint) error {
	var (
		// At this point, we've already verified that the given endpoint's request
		// is a wrapper, so we can safely access it without any nil-checks.
		bodyField  = endpoint.SdkRequest.Shape.Wrapper.BodyKey.PascalCase.UnsafeName
		typeName   = endpoint.SdkRequest.Shape.Wrapper.WrapperName.PascalCase.UnsafeName
		receiver   = typeNameToReceiver(typeName)
		importPath = fernFilepathToImportPath(f.baseImportPath, fernFilepath)
	)

	f.P("type ", typeName, " struct {")
	for _, header := range endpoint.Headers {
		f.P(header.Name.Name.PascalCase.UnsafeName, " ", typeReferenceToGoType(header.ValueType, f.types, f.imports, f.baseImportPath, importPath), " `json:\"-\"`")
	}
	for _, queryParam := range endpoint.QueryParameters {
		value := typeReferenceToGoType(queryParam.ValueType, f.types, f.imports, f.baseImportPath, importPath)
		if queryParam.AllowMultiple {
			// TODO: If the query parameter can be specified multiple times, it's not enough to just define it
			// as a list. Otherwise, it's indistinguishable from a single query parameter with a list value.
			//
			// We'll need to track how the query parameter is applied at the call-site.
			value = fmt.Sprintf("[]%s", value)
		}
		f.P(queryParam.Name.Name.PascalCase.UnsafeName, " ", value, " `json:\"-\"`")
	}
	if endpoint.RequestBody == nil {
		// If the request doesn't have a body, we don't need any custom [de]serialization logic.
		f.P("}")
		f.P()
		return nil
	}
	literals, err := requestBodyToFieldDeclaration(endpoint.RequestBody, f, importPath, bodyField)
	if err != nil {
		return err
	}
	f.P("}")
	f.P()

	// Implement the getter methods.
	for _, literal := range literals {
		f.P("func (", receiver, " *", typeName, ") ", literal.Name.PascalCase.UnsafeName, "()", literalToGoType(literal.Value), "{")
		f.P("return ", receiver, ".", literal.Name.CamelCase.SafeName)
		f.P("}")
		f.P()
	}

	var referenceType string
	var referenceIsPointer bool
	var referenceLiteral string
	if reference := endpoint.RequestBody.Reference; reference != nil {
		referenceType = strings.TrimPrefix(
			typeReferenceToGoType(reference.RequestBodyType, f.types, f.imports, f.baseImportPath, importPath),
			"*",
		)
		referenceIsPointer = reference.RequestBodyType.Named != nil && isPointer(f.types[reference.RequestBodyType.Named.TypeId])
		if reference.RequestBodyType.Container != nil && reference.RequestBodyType.Container.Literal != nil {
			referenceLiteral = literalToValue(reference.RequestBodyType.Container.Literal)
		}
	}

	if len(literals) == 0 && len(referenceType) == 0 {
		// If the request doesn't specify any literals or a reference type,
		// we don't need to customize the [de]serialization logic at all.
		return nil
	}

	// Implement the json.Unmarshaler interface.
	f.P("func (", receiver, " *", typeName, ") UnmarshalJSON(data []byte) error {")
	if len(referenceType) > 0 {
		if referenceIsPointer {
			f.P("body := new(", referenceType, ")")
		} else {
			f.P("var body ", referenceType)
		}
	} else {
		f.P("type unmarshaler ", typeName)
		f.P("var body unmarshaler")
	}
	f.P("if err := json.Unmarshal(data, &body); err != nil {")
	f.P("return err")
	f.P("}")
	if len(referenceType) > 0 {
		if len(referenceLiteral) > 0 {
			f.P("if body != ", referenceLiteral, "{")
			f.P(`return fmt.Errorf("expected literal %q, but found %q", `, referenceLiteral, ", body)")
			f.P("}")
		}
		f.P(receiver, ".", bodyField, " = body")
	} else {
		f.P("*", receiver, " = ", typeName, "(body)")
	}
	for _, literal := range literals {
		f.P(receiver, ".", literal.Name.CamelCase.SafeName, " = ", literalToValue(literal.Value))
	}
	f.P("return nil")
	f.P("}")
	f.P()

	// Implement the json.Marshaler interface.
	f.P("func (", receiver, " *", typeName, ") MarshalJSON() ([]byte, error) {")
	if len(referenceType) > 0 {
		// If the request body is a reference type, we only need to marshal the body.
		value := fmt.Sprintf("%s.%s", receiver, bodyField)
		if len(referenceLiteral) > 0 {
			value = referenceLiteral
		}
		f.P("return json.Marshal(", value, ")")
	} else {
		f.P("type embed ", typeName)
		f.P("var marshaler = struct{")
		f.P("embed")
		for _, literal := range literals {
			f.P(literal.Name.PascalCase.UnsafeName, " ", literalToGoType(literal.Value), " `json:\"", literal.Name.OriginalName, "\"`")
		}
		f.P("}{")
		f.P("embed: embed(*", receiver, "),")
		for _, literal := range literals {
			f.P(literal.Name.PascalCase.UnsafeName, ": ", literalToValue(literal.Value), ",")
		}
		f.P("}")
		f.P("return json.Marshal(marshaler)")
	}
	f.P("}")
	f.P()

	return nil
}

func requestBodyToFieldDeclaration(
	requestBody *ir.HttpRequestBody,
	writer *fileWriter,
	importPath string,
	bodyField string,
) ([]*literal, error) {
	visitor := &requestBodyVisitor{
		bodyField:      bodyField,
		baseImportPath: writer.baseImportPath,
		importPath:     importPath,
		imports:        writer.imports,
		types:          writer.types,
		writer:         writer,
	}
	if err := requestBody.Accept(visitor); err != nil {
		return nil, err
	}
	return visitor.literals, nil
}

type requestBodyVisitor struct {
	literals       []*literal
	bodyField      string
	baseImportPath string
	importPath     string
	imports        imports
	types          map[ir.TypeId]*ir.TypeDeclaration
	writer         *fileWriter
}

func (r *requestBodyVisitor) VisitInlinedRequestBody(inlinedRequestBody *ir.InlinedRequestBody) error {
	typeVisitor := &typeVisitor{
		typeName:       inlinedRequestBody.Name.PascalCase.UnsafeName,
		baseImportPath: r.baseImportPath,
		importPath:     r.importPath,
		writer:         r.writer,
	}
	objectTypeDeclaration := inlinedRequestBodyToObjectTypeDeclaration(inlinedRequestBody)
	_, literals := typeVisitor.visitObjectProperties(objectTypeDeclaration, true /* includeTags */)
	r.literals = literals
	return nil
}

func (r *requestBodyVisitor) VisitReference(reference *ir.HttpRequestBodyReference) error {
	// For references, we include the type in a field that matches the configured body key.
	r.writer.P(
		r.bodyField,
		" ",
		typeReferenceToGoType(reference.RequestBodyType, r.types, r.imports, r.baseImportPath, r.importPath),
		" `json:\"-\"`",
	)
	return nil
}

func (r *requestBodyVisitor) VisitFileUpload(fileUpload *ir.FileUploadRequest) error {
	return errors.New("file upload requests are not yet supported")
}

// inlinedRequestBodyToObjectTypeDeclaration maps the given inlined request body
// into an object type declaration so that we can reuse the functionality required
// to write object properties for a generated object.
func inlinedRequestBodyToObjectTypeDeclaration(inlinedRequestBody *ir.InlinedRequestBody) *ir.ObjectTypeDeclaration {
	properties := make([]*ir.ObjectProperty, len(inlinedRequestBody.Properties))
	for i, property := range inlinedRequestBody.Properties {
		properties[i] = &ir.ObjectProperty{
			Docs:      property.Docs,
			Name:      property.Name,
			ValueType: property.ValueType,
		}
	}
	return &ir.ObjectTypeDeclaration{
		Extends:    inlinedRequestBody.Extends,
		Properties: properties,
	}
}

// irMethodToMethodEnum maps the given ir.HttpMethod to the net/http equivalent.
// Note this returns the string representation of the net/http constant (e.g.
// "http.MethodGet"), not the value the constant points to (e.g. "GET").
func irMethodToMethodEnum(method ir.HttpMethod) string {
	switch method {
	case ir.HttpMethodGet:
		return "http.MethodGet"
	case ir.HttpMethodPost:
		return "http.MethodPost"
	case ir.HttpMethodPut:
		return "http.MethodPut"
	case ir.HttpMethodPatch:
		return "http.MethodPatch"
	case ir.HttpMethodDelete:
		return "http.MethodDelete"
	}
	return ""
}
