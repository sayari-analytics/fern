# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .test_submission_update_info import TestSubmissionUpdateInfo


class TestSubmissionUpdate(pydantic.BaseModel):
    update_time: dt.datetime = pydantic.Field(alias="updateTime")
    update_info: TestSubmissionUpdateInfo = pydantic.Field(alias="updateInfo")

    class Partial(typing_extensions.TypedDict):
        update_time: typing_extensions.NotRequired[dt.datetime]
        update_info: typing_extensions.NotRequired[TestSubmissionUpdateInfo]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestSubmissionUpdate.Validators.root
            def validate(values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdate.Partial:
                ...

            @TestSubmissionUpdate.Validators.field("update_time")
            def validate_update_time(update_time: dt.datetime, values: TestSubmissionUpdate.Partial) -> dt.datetime:
                ...

            @TestSubmissionUpdate.Validators.field("update_info")
            def validate_update_info(update_info: TestSubmissionUpdateInfo, values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdateInfo:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestSubmissionUpdate.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestSubmissionUpdate.Validators._RootValidator]] = []
        _update_time_pre_validators: typing.ClassVar[
            typing.List[TestSubmissionUpdate.Validators.UpdateTimeValidator]
        ] = []
        _update_time_post_validators: typing.ClassVar[
            typing.List[TestSubmissionUpdate.Validators.UpdateTimeValidator]
        ] = []
        _update_info_pre_validators: typing.ClassVar[
            typing.List[TestSubmissionUpdate.Validators.UpdateInfoValidator]
        ] = []
        _update_info_post_validators: typing.ClassVar[
            typing.List[TestSubmissionUpdate.Validators.UpdateInfoValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> TestSubmissionUpdate.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["update_time"]
        ) -> typing.Callable[
            [TestSubmissionUpdate.Validators.UpdateTimeValidator], TestSubmissionUpdate.Validators.UpdateTimeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["update_info"]
        ) -> typing.Callable[
            [TestSubmissionUpdate.Validators.UpdateInfoValidator], TestSubmissionUpdate.Validators.UpdateInfoValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "update_time":
                    if pre:
                        cls._update_time_pre_validators.append(validator)
                    else:
                        cls._update_time_post_validators.append(validator)
                if field_name == "update_info":
                    if pre:
                        cls._update_info_pre_validators.append(validator)
                    else:
                        cls._update_info_post_validators.append(validator)
                return validator

            return decorator

        class UpdateTimeValidator(typing_extensions.Protocol):
            def __call__(self, __v: dt.datetime, __values: TestSubmissionUpdate.Partial) -> dt.datetime:
                ...

        class UpdateInfoValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestSubmissionUpdateInfo, __values: TestSubmissionUpdate.Partial
            ) -> TestSubmissionUpdateInfo:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdate.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdate.Partial:
        for validator in TestSubmissionUpdate.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdate.Partial:
        for validator in TestSubmissionUpdate.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("update_time", pre=True)
    def _pre_validate_update_time(cls, v: dt.datetime, values: TestSubmissionUpdate.Partial) -> dt.datetime:
        for validator in TestSubmissionUpdate.Validators._update_time_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("update_time", pre=False)
    def _post_validate_update_time(cls, v: dt.datetime, values: TestSubmissionUpdate.Partial) -> dt.datetime:
        for validator in TestSubmissionUpdate.Validators._update_time_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("update_info", pre=True)
    def _pre_validate_update_info(
        cls, v: TestSubmissionUpdateInfo, values: TestSubmissionUpdate.Partial
    ) -> TestSubmissionUpdateInfo:
        for validator in TestSubmissionUpdate.Validators._update_info_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("update_info", pre=False)
    def _post_validate_update_info(
        cls, v: TestSubmissionUpdateInfo, values: TestSubmissionUpdate.Partial
    ) -> TestSubmissionUpdateInfo:
        for validator in TestSubmissionUpdate.Validators._update_info_post_validators:
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
