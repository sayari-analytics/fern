/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.trace.resources.v2;

import com.seed.trace.core.ApiError;
import com.seed.trace.core.ClientOptions;
import com.seed.trace.core.ObjectMappers;
import com.seed.trace.core.RequestOptions;
import com.seed.trace.core.Suppliers;
import com.seed.trace.resources.v2.problem.ProblemClient;
import com.seed.trace.resources.v2.v3.V3Client;
import java.io.IOException;
import java.util.function.Supplier;
import okhttp3.Headers;
import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class V2Client {
    protected final ClientOptions clientOptions;

    protected final Supplier<ProblemClient> problemClient;

    protected final Supplier<V3Client> v3Client;

    public V2Client(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
        this.problemClient = Suppliers.memoize(() -> new ProblemClient(clientOptions));
        this.v3Client = Suppliers.memoize(() -> new V3Client(clientOptions));
    }

    public void test() {
        test(null);
    }

    public void test(RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .build();
        Request okhttpRequest = new Request.Builder()
                .url(httpUrl)
                .method("GET", null)
                .headers(Headers.of(clientOptions.headers(requestOptions)))
                .build();
        try {
            OkHttpClient client = clientOptions.httpClient();
            if (requestOptions != null && requestOptions.getTimeout().isPresent()) {
                client = clientOptions.httpClientWithTimeout(requestOptions);
            }
            Response response = client.newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return;
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public ProblemClient problem() {
        return this.problemClient.get();
    }

    public V3Client v3() {
        return this.v3Client.get();
    }
}