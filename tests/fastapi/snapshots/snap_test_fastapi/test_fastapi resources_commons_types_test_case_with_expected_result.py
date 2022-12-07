# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case import TestCase
from .variable_value import VariableValue


class TestCaseWithExpectedResult(pydantic.BaseModel):
    test_case: TestCase = pydantic.Field(alias="testCase")
    expected_result: VariableValue = pydantic.Field(alias="expectedResult")

    class Partial(typing_extensions.TypedDict):
        test_case: typing_extensions.NotRequired[TestCase]
        expected_result: typing_extensions.NotRequired[VariableValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseWithExpectedResult.Validators.root
            def validate(values: TestCaseWithExpectedResult.Partial) -> TestCaseWithExpectedResult.Partial:
                ...

            @TestCaseWithExpectedResult.Validators.field("test_case")
            def validate_test_case(test_case: TestCase, values: TestCaseWithExpectedResult.Partial) -> TestCase:
                ...

            @TestCaseWithExpectedResult.Validators.field("expected_result")
            def validate_expected_result(expected_result: VariableValue, values: TestCaseWithExpectedResult.Partial) -> VariableValue:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCaseWithExpectedResult.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCaseWithExpectedResult.Validators._RootValidator]] = []
        _test_case_pre_validators: typing.ClassVar[
            typing.List[TestCaseWithExpectedResult.Validators.TestCaseValidator]
        ] = []
        _test_case_post_validators: typing.ClassVar[
            typing.List[TestCaseWithExpectedResult.Validators.TestCaseValidator]
        ] = []
        _expected_result_pre_validators: typing.ClassVar[
            typing.List[TestCaseWithExpectedResult.Validators.ExpectedResultValidator]
        ] = []
        _expected_result_post_validators: typing.ClassVar[
            typing.List[TestCaseWithExpectedResult.Validators.ExpectedResultValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> TestCaseWithExpectedResult.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["test_case"]
        ) -> typing.Callable[
            [TestCaseWithExpectedResult.Validators.TestCaseValidator],
            TestCaseWithExpectedResult.Validators.TestCaseValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_result"]
        ) -> typing.Callable[
            [TestCaseWithExpectedResult.Validators.ExpectedResultValidator],
            TestCaseWithExpectedResult.Validators.ExpectedResultValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "test_case":
                    if pre:
                        cls._test_case_pre_validators.append(validator)
                    else:
                        cls._test_case_post_validators.append(validator)
                if field_name == "expected_result":
                    if pre:
                        cls._expected_result_pre_validators.append(validator)
                    else:
                        cls._expected_result_post_validators.append(validator)
                return validator

            return decorator

        class TestCaseValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCase, __values: TestCaseWithExpectedResult.Partial) -> TestCase:
                ...

        class ExpectedResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableValue, __values: TestCaseWithExpectedResult.Partial) -> VariableValue:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCaseWithExpectedResult.Partial) -> TestCaseWithExpectedResult.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestCaseWithExpectedResult.Partial) -> TestCaseWithExpectedResult.Partial:
        for validator in TestCaseWithExpectedResult.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestCaseWithExpectedResult.Partial) -> TestCaseWithExpectedResult.Partial:
        for validator in TestCaseWithExpectedResult.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("test_case", pre=True)
    def _pre_validate_test_case(cls, v: TestCase, values: TestCaseWithExpectedResult.Partial) -> TestCase:
        for validator in TestCaseWithExpectedResult.Validators._test_case_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case", pre=False)
    def _post_validate_test_case(cls, v: TestCase, values: TestCaseWithExpectedResult.Partial) -> TestCase:
        for validator in TestCaseWithExpectedResult.Validators._test_case_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_result", pre=True)
    def _pre_validate_expected_result(
        cls, v: VariableValue, values: TestCaseWithExpectedResult.Partial
    ) -> VariableValue:
        for validator in TestCaseWithExpectedResult.Validators._expected_result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_result", pre=False)
    def _post_validate_expected_result(
        cls, v: VariableValue, values: TestCaseWithExpectedResult.Partial
    ) -> VariableValue:
        for validator in TestCaseWithExpectedResult.Validators._expected_result_post_validators:
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
