# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class SubmissionFileInfo(pydantic.BaseModel):
    directory: str
    filename: str
    contents: str

    class Partial(typing_extensions.TypedDict):
        directory: typing_extensions.NotRequired[str]
        filename: typing_extensions.NotRequired[str]
        contents: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionFileInfo.Validators.root
            def validate(values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
                ...

            @SubmissionFileInfo.Validators.field("directory")
            def validate_directory(directory: str, values: SubmissionFileInfo.Partial) -> str:
                ...

            @SubmissionFileInfo.Validators.field("filename")
            def validate_filename(filename: str, values: SubmissionFileInfo.Partial) -> str:
                ...

            @SubmissionFileInfo.Validators.field("contents")
            def validate_contents(contents: str, values: SubmissionFileInfo.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators._RootValidator]] = []
        _directory_pre_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.DirectoryValidator]] = []
        _directory_post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.DirectoryValidator]] = []
        _filename_pre_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.FilenameValidator]] = []
        _filename_post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.FilenameValidator]] = []
        _contents_pre_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.ContentsValidator]] = []
        _contents_post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.ContentsValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> SubmissionFileInfo.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["directory"]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.DirectoryValidator], SubmissionFileInfo.Validators.DirectoryValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.FilenameValidator], SubmissionFileInfo.Validators.FilenameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.ContentsValidator], SubmissionFileInfo.Validators.ContentsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "directory":
                    if pre:
                        cls._directory_pre_validators.append(validator)
                    else:
                        cls._directory_post_validators.append(validator)
                if field_name == "filename":
                    if pre:
                        cls._filename_pre_validators.append(validator)
                    else:
                        cls._filename_post_validators.append(validator)
                if field_name == "contents":
                    if pre:
                        cls._contents_pre_validators.append(validator)
                    else:
                        cls._contents_post_validators.append(validator)
                return validator

            return decorator

        class DirectoryValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: SubmissionFileInfo.Partial) -> str:
                ...

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: SubmissionFileInfo.Partial) -> str:
                ...

        class ContentsValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: SubmissionFileInfo.Partial) -> str:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
        for validator in SubmissionFileInfo.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
        for validator in SubmissionFileInfo.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("directory", pre=True)
    def _pre_validate_directory(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._directory_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("directory", pre=False)
    def _post_validate_directory(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._directory_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=True)
    def _pre_validate_filename(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._filename_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=False)
    def _post_validate_filename(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._filename_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=True)
    def _pre_validate_contents(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._contents_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=False)
    def _post_validate_contents(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._contents_post_validators:
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
        extra = pydantic.Extra.forbid
