# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class GenericValue(pydantic.BaseModel):
    stringified_type: typing.Optional[str] = pydantic.Field(alias="stringifiedType")
    stringified_value: str = pydantic.Field(alias="stringifiedValue")

    class Partial(typing_extensions.TypedDict):
        stringified_type: typing_extensions.NotRequired[typing.Optional[str]]
        stringified_value: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GenericValue.Validators.root
            def validate(values: GenericValue.Partial) -> GenericValue.Partial:
                ...

            @GenericValue.Validators.field("stringified_type")
            def validate_stringified_type(stringified_type: typing.Optional[str], values: GenericValue.Partial) -> typing.Optional[str]:
                ...

            @GenericValue.Validators.field("stringified_value")
            def validate_stringified_value(stringified_value: str, values: GenericValue.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GenericValue.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GenericValue.Validators._RootValidator]] = []
        _stringified_type_pre_validators: typing.ClassVar[
            typing.List[GenericValue.Validators.StringifiedTypeValidator]
        ] = []
        _stringified_type_post_validators: typing.ClassVar[
            typing.List[GenericValue.Validators.StringifiedTypeValidator]
        ] = []
        _stringified_value_pre_validators: typing.ClassVar[
            typing.List[GenericValue.Validators.StringifiedValueValidator]
        ] = []
        _stringified_value_post_validators: typing.ClassVar[
            typing.List[GenericValue.Validators.StringifiedValueValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> GenericValue.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["stringified_type"]
        ) -> typing.Callable[
            [GenericValue.Validators.StringifiedTypeValidator], GenericValue.Validators.StringifiedTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stringified_value"]
        ) -> typing.Callable[
            [GenericValue.Validators.StringifiedValueValidator], GenericValue.Validators.StringifiedValueValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "stringified_type":
                    if pre:
                        cls._stringified_type_pre_validators.append(validator)
                    else:
                        cls._stringified_type_post_validators.append(validator)
                if field_name == "stringified_value":
                    if pre:
                        cls._stringified_value_pre_validators.append(validator)
                    else:
                        cls._stringified_value_post_validators.append(validator)
                return validator

            return decorator

        class StringifiedTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: GenericValue.Partial) -> typing.Optional[str]:
                ...

        class StringifiedValueValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GenericValue.Partial) -> str:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GenericValue.Partial) -> GenericValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: GenericValue.Partial) -> GenericValue.Partial:
        for validator in GenericValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: GenericValue.Partial) -> GenericValue.Partial:
        for validator in GenericValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("stringified_type", pre=True)
    def _pre_validate_stringified_type(
        cls, v: typing.Optional[str], values: GenericValue.Partial
    ) -> typing.Optional[str]:
        for validator in GenericValue.Validators._stringified_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stringified_type", pre=False)
    def _post_validate_stringified_type(
        cls, v: typing.Optional[str], values: GenericValue.Partial
    ) -> typing.Optional[str]:
        for validator in GenericValue.Validators._stringified_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stringified_value", pre=True)
    def _pre_validate_stringified_value(cls, v: str, values: GenericValue.Partial) -> str:
        for validator in GenericValue.Validators._stringified_value_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stringified_value", pre=False)
    def _post_validate_stringified_value(cls, v: str, values: GenericValue.Partial) -> str:
        for validator in GenericValue.Validators._stringified_value_post_validators:
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
