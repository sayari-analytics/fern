# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..submission.types.submission_id import SubmissionId
from ..submission.types.test_case_result_with_stdout import TestCaseResultWithStdout
from ..submission.types.test_submission_status import TestSubmissionStatus
from ..submission.types.test_submission_update import TestSubmissionUpdate
from ..submission.types.trace_response import TraceResponse
from ..submission.types.trace_response_v_2 import TraceResponseV2
from ..submission.types.workspace_run_details import WorkspaceRunDetails
from ..submission.types.workspace_submission_status import WorkspaceSubmissionStatus
from ..submission.types.workspace_submission_update import WorkspaceSubmissionUpdate
from ..v_2.resources.problem.types.test_case_id import TestCaseId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def update_test_submission_status(
        self,
        submission_id: SubmissionId,
        *,
        request: TestSubmissionStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: TestSubmissionStatus.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-submission-status/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def send_test_submission_update(
        self,
        submission_id: SubmissionId,
        *,
        request: TestSubmissionUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: TestSubmissionUpdate.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-submission-status-v2/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_workspace_submission_status(
        self,
        submission_id: SubmissionId,
        *,
        request: WorkspaceSubmissionStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: WorkspaceSubmissionStatus.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-submission-status/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def send_workspace_submission_update(
        self,
        submission_id: SubmissionId,
        *,
        request: WorkspaceSubmissionUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: WorkspaceSubmissionUpdate.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-submission-status-v2/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def store_traced_test_case(
        self,
        submission_id: SubmissionId,
        test_case_id: str,
        *,
        result: TestCaseResultWithStdout,
        trace_responses: typing.Sequence[TraceResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - test_case_id: str.

            - result: TestCaseResultWithStdout.

            - trace_responses: typing.Sequence[TraceResponse].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-trace/submission/{jsonable_encoder(submission_id)}/testCase/{jsonable_encoder(test_case_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"result": result, "traceResponses": trace_responses})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"result": result, "traceResponses": trace_responses}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def store_traced_test_case_v_2(
        self,
        submission_id: SubmissionId,
        test_case_id: TestCaseId,
        *,
        request: typing.Sequence[TraceResponseV2],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - test_case_id: TestCaseId.

            - request: typing.Sequence[TraceResponseV2].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-trace-v2/submission/{jsonable_encoder(submission_id)}/testCase/{jsonable_encoder(test_case_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def store_traced_workspace(
        self,
        submission_id: SubmissionId,
        *,
        workspace_run_details: WorkspaceRunDetails,
        trace_responses: typing.Sequence[TraceResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - workspace_run_details: WorkspaceRunDetails.

            - trace_responses: typing.Sequence[TraceResponse].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-trace/submission/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"workspaceRunDetails": workspace_run_details, "traceResponses": trace_responses})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"workspaceRunDetails": workspace_run_details, "traceResponses": trace_responses}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def store_traced_workspace_v_2(
        self,
        submission_id: SubmissionId,
        *,
        request: typing.Sequence[TraceResponseV2],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: typing.Sequence[TraceResponseV2].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-trace-v2/submission/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def update_test_submission_status(
        self,
        submission_id: SubmissionId,
        *,
        request: TestSubmissionStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: TestSubmissionStatus.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-submission-status/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def send_test_submission_update(
        self,
        submission_id: SubmissionId,
        *,
        request: TestSubmissionUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: TestSubmissionUpdate.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-submission-status-v2/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_workspace_submission_status(
        self,
        submission_id: SubmissionId,
        *,
        request: WorkspaceSubmissionStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: WorkspaceSubmissionStatus.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-submission-status/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def send_workspace_submission_update(
        self,
        submission_id: SubmissionId,
        *,
        request: WorkspaceSubmissionUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: WorkspaceSubmissionUpdate.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-submission-status-v2/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def store_traced_test_case(
        self,
        submission_id: SubmissionId,
        test_case_id: str,
        *,
        result: TestCaseResultWithStdout,
        trace_responses: typing.Sequence[TraceResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - test_case_id: str.

            - result: TestCaseResultWithStdout.

            - trace_responses: typing.Sequence[TraceResponse].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-trace/submission/{jsonable_encoder(submission_id)}/testCase/{jsonable_encoder(test_case_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"result": result, "traceResponses": trace_responses})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"result": result, "traceResponses": trace_responses}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def store_traced_test_case_v_2(
        self,
        submission_id: SubmissionId,
        test_case_id: TestCaseId,
        *,
        request: typing.Sequence[TraceResponseV2],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - test_case_id: TestCaseId.

            - request: typing.Sequence[TraceResponseV2].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-test-trace-v2/submission/{jsonable_encoder(submission_id)}/testCase/{jsonable_encoder(test_case_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def store_traced_workspace(
        self,
        submission_id: SubmissionId,
        *,
        workspace_run_details: WorkspaceRunDetails,
        trace_responses: typing.Sequence[TraceResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - workspace_run_details: WorkspaceRunDetails.

            - trace_responses: typing.Sequence[TraceResponse].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-trace/submission/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"workspaceRunDetails": workspace_run_details, "traceResponses": trace_responses})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"workspaceRunDetails": workspace_run_details, "traceResponses": trace_responses}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def store_traced_workspace_v_2(
        self,
        submission_id: SubmissionId,
        *,
        request: typing.Sequence[TraceResponseV2],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - submission_id: SubmissionId.

            - request: typing.Sequence[TraceResponseV2].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"admin/store-workspace-trace-v2/submission/{jsonable_encoder(submission_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
