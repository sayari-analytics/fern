# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...v_2.problem.types.test_case_id import TestCaseId
from .submission_id import SubmissionId
from .test_case_grade import TestCaseGrade


class GradedResponseV2(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    test_cases: typing.Dict[TestCaseId, TestCaseGrade] = pydantic.Field(alias="testCases")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        test_cases: typing_extensions.NotRequired[typing.Dict[TestCaseId, TestCaseGrade]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GradedResponseV2.Validators.root
            def validate(values: GradedResponseV2.Partial) -> GradedResponseV2.Partial:
                ...

            @GradedResponseV2.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: GradedResponseV2.Partial) -> SubmissionId:
                ...

            @GradedResponseV2.Validators.field("test_cases")
            def validate_test_cases(test_cases: typing.Dict[TestCaseId, TestCaseGrade], values: GradedResponseV2.Partial) -> typing.Dict[TestCaseId, TestCaseGrade]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GradedResponseV2.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GradedResponseV2.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[GradedResponseV2.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[GradedResponseV2.Validators.SubmissionIdValidator]
        ] = []
        _test_cases_pre_validators: typing.ClassVar[typing.List[GradedResponseV2.Validators.TestCasesValidator]] = []
        _test_cases_post_validators: typing.ClassVar[typing.List[GradedResponseV2.Validators.TestCasesValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> GradedResponseV2.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [GradedResponseV2.Validators.SubmissionIdValidator], GradedResponseV2.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_cases"]
        ) -> typing.Callable[
            [GradedResponseV2.Validators.TestCasesValidator], GradedResponseV2.Validators.TestCasesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "test_cases":
                    if pre:
                        cls._test_cases_pre_validators.append(validator)
                    else:
                        cls._test_cases_post_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: GradedResponseV2.Partial) -> SubmissionId:
                ...

        class TestCasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[TestCaseId, TestCaseGrade], __values: GradedResponseV2.Partial
            ) -> typing.Dict[TestCaseId, TestCaseGrade]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GradedResponseV2.Partial) -> GradedResponseV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: GradedResponseV2.Partial) -> GradedResponseV2.Partial:
        for validator in GradedResponseV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: GradedResponseV2.Partial) -> GradedResponseV2.Partial:
        for validator in GradedResponseV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: GradedResponseV2.Partial) -> SubmissionId:
        for validator in GradedResponseV2.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: GradedResponseV2.Partial) -> SubmissionId:
        for validator in GradedResponseV2.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_cases", pre=True)
    def _pre_validate_test_cases(
        cls, v: typing.Dict[TestCaseId, TestCaseGrade], values: GradedResponseV2.Partial
    ) -> typing.Dict[TestCaseId, TestCaseGrade]:
        for validator in GradedResponseV2.Validators._test_cases_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_cases", pre=False)
    def _post_validate_test_cases(
        cls, v: typing.Dict[TestCaseId, TestCaseGrade], values: GradedResponseV2.Partial
    ) -> typing.Dict[TestCaseId, TestCaseGrade]:
        for validator in GradedResponseV2.Validators._test_cases_post_validators:
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
        extra = pydantic.Extra.forbid
