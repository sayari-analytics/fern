# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.problem_id import ProblemId
from ..commons.test_case import TestCase
from .test_submission_status import TestSubmissionStatus


class TestSubmissionState(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    default_test_cases: typing.List[TestCase] = pydantic.Field(alias="defaultTestCases")
    custom_test_cases: typing.List[TestCase] = pydantic.Field(alias="customTestCases")
    status: TestSubmissionStatus

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        default_test_cases: typing_extensions.NotRequired[typing.List[TestCase]]
        custom_test_cases: typing_extensions.NotRequired[typing.List[TestCase]]
        status: typing_extensions.NotRequired[TestSubmissionStatus]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestSubmissionState.Validators.root
            def validate(values: TestSubmissionState.Partial) -> TestSubmissionState.Partial:
                ...

            @TestSubmissionState.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: TestSubmissionState.Partial) -> ProblemId:
                ...

            @TestSubmissionState.Validators.field("default_test_cases")
            def validate_default_test_cases(default_test_cases: typing.List[TestCase], values: TestSubmissionState.Partial) -> typing.List[TestCase]:
                ...

            @TestSubmissionState.Validators.field("custom_test_cases")
            def validate_custom_test_cases(custom_test_cases: typing.List[TestCase], values: TestSubmissionState.Partial) -> typing.List[TestCase]:
                ...

            @TestSubmissionState.Validators.field("status")
            def validate_status(status: TestSubmissionStatus, values: TestSubmissionState.Partial) -> TestSubmissionStatus:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestSubmissionState.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestSubmissionState.Validators._RootValidator]] = []
        _problem_id_pre_validators: typing.ClassVar[typing.List[TestSubmissionState.Validators.ProblemIdValidator]] = []
        _problem_id_post_validators: typing.ClassVar[
            typing.List[TestSubmissionState.Validators.ProblemIdValidator]
        ] = []
        _default_test_cases_pre_validators: typing.ClassVar[
            typing.List[TestSubmissionState.Validators.DefaultTestCasesValidator]
        ] = []
        _default_test_cases_post_validators: typing.ClassVar[
            typing.List[TestSubmissionState.Validators.DefaultTestCasesValidator]
        ] = []
        _custom_test_cases_pre_validators: typing.ClassVar[
            typing.List[TestSubmissionState.Validators.CustomTestCasesValidator]
        ] = []
        _custom_test_cases_post_validators: typing.ClassVar[
            typing.List[TestSubmissionState.Validators.CustomTestCasesValidator]
        ] = []
        _status_pre_validators: typing.ClassVar[typing.List[TestSubmissionState.Validators.StatusValidator]] = []
        _status_post_validators: typing.ClassVar[typing.List[TestSubmissionState.Validators.StatusValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> TestSubmissionState.Validators._RootValidator:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.ProblemIdValidator], TestSubmissionState.Validators.ProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["default_test_cases"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.DefaultTestCasesValidator],
            TestSubmissionState.Validators.DefaultTestCasesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_test_cases"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.CustomTestCasesValidator],
            TestSubmissionState.Validators.CustomTestCasesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.StatusValidator], TestSubmissionState.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    if pre:
                        cls._problem_id_pre_validators.append(validator)
                    else:
                        cls._problem_id_post_validators.append(validator)
                if field_name == "default_test_cases":
                    if pre:
                        cls._default_test_cases_pre_validators.append(validator)
                    else:
                        cls._default_test_cases_post_validators.append(validator)
                if field_name == "custom_test_cases":
                    if pre:
                        cls._custom_test_cases_pre_validators.append(validator)
                    else:
                        cls._custom_test_cases_post_validators.append(validator)
                if field_name == "status":
                    if pre:
                        cls._status_pre_validators.append(validator)
                    else:
                        cls._status_post_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: TestSubmissionState.Partial) -> ProblemId:
                ...

        class DefaultTestCasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCase], __values: TestSubmissionState.Partial
            ) -> typing.List[TestCase]:
                ...

        class CustomTestCasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCase], __values: TestSubmissionState.Partial
            ) -> typing.List[TestCase]:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestSubmissionStatus, __values: TestSubmissionState.Partial
            ) -> TestSubmissionStatus:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestSubmissionState.Partial) -> TestSubmissionState.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestSubmissionState.Partial) -> TestSubmissionState.Partial:
        for validator in TestSubmissionState.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestSubmissionState.Partial) -> TestSubmissionState.Partial:
        for validator in TestSubmissionState.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_id", pre=True)
    def _pre_validate_problem_id(cls, v: ProblemId, values: TestSubmissionState.Partial) -> ProblemId:
        for validator in TestSubmissionState.Validators._problem_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=False)
    def _post_validate_problem_id(cls, v: ProblemId, values: TestSubmissionState.Partial) -> ProblemId:
        for validator in TestSubmissionState.Validators._problem_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("default_test_cases", pre=True)
    def _pre_validate_default_test_cases(
        cls, v: typing.List[TestCase], values: TestSubmissionState.Partial
    ) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._default_test_cases_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("default_test_cases", pre=False)
    def _post_validate_default_test_cases(
        cls, v: typing.List[TestCase], values: TestSubmissionState.Partial
    ) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._default_test_cases_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_test_cases", pre=True)
    def _pre_validate_custom_test_cases(
        cls, v: typing.List[TestCase], values: TestSubmissionState.Partial
    ) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._custom_test_cases_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_test_cases", pre=False)
    def _post_validate_custom_test_cases(
        cls, v: typing.List[TestCase], values: TestSubmissionState.Partial
    ) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._custom_test_cases_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=True)
    def _pre_validate_status(cls, v: TestSubmissionStatus, values: TestSubmissionState.Partial) -> TestSubmissionStatus:
        for validator in TestSubmissionState.Validators._status_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=False)
    def _post_validate_status(
        cls, v: TestSubmissionStatus, values: TestSubmissionState.Partial
    ) -> TestSubmissionStatus:
        for validator in TestSubmissionState.Validators._status_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
