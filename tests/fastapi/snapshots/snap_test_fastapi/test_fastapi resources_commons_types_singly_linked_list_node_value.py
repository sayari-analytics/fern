# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .node_id import NodeId


class SinglyLinkedListNodeValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    val: float
    next: typing.Optional[NodeId]

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        val: typing_extensions.NotRequired[float]
        next: typing_extensions.NotRequired[typing.Optional[NodeId]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SinglyLinkedListNodeValue.Validators.root
            def validate(values: SinglyLinkedListNodeValue.Partial) -> SinglyLinkedListNodeValue.Partial:
                ...

            @SinglyLinkedListNodeValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: SinglyLinkedListNodeValue.Partial) -> NodeId:
                ...

            @SinglyLinkedListNodeValue.Validators.field("val")
            def validate_val(val: float, values: SinglyLinkedListNodeValue.Partial) -> float:
                ...

            @SinglyLinkedListNodeValue.Validators.field("next")
            def validate_next(next: typing.Optional[NodeId], values: SinglyLinkedListNodeValue.Partial) -> typing.Optional[NodeId]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeValue.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeValue.Validators._RootValidator]] = []
        _node_id_pre_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeValue.Validators.NodeIdValidator]] = []
        _node_id_post_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeValue.Validators.NodeIdValidator]
        ] = []
        _val_pre_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeValue.Validators.ValValidator]] = []
        _val_post_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeValue.Validators.ValValidator]] = []
        _next_pre_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeValue.Validators.NextValidator]] = []
        _next_post_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeValue.Validators.NextValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> SinglyLinkedListNodeValue.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["node_id"]
        ) -> typing.Callable[
            [SinglyLinkedListNodeValue.Validators.NodeIdValidator], SinglyLinkedListNodeValue.Validators.NodeIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["val"]
        ) -> typing.Callable[
            [SinglyLinkedListNodeValue.Validators.ValValidator], SinglyLinkedListNodeValue.Validators.ValValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["next"]
        ) -> typing.Callable[
            [SinglyLinkedListNodeValue.Validators.NextValidator], SinglyLinkedListNodeValue.Validators.NextValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    if pre:
                        cls._node_id_pre_validators.append(validator)
                    else:
                        cls._node_id_post_validators.append(validator)
                if field_name == "val":
                    if pre:
                        cls._val_pre_validators.append(validator)
                    else:
                        cls._val_post_validators.append(validator)
                if field_name == "next":
                    if pre:
                        cls._next_pre_validators.append(validator)
                    else:
                        cls._next_post_validators.append(validator)
                return validator

            return decorator

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: NodeId, __values: SinglyLinkedListNodeValue.Partial) -> NodeId:
                ...

        class ValValidator(typing_extensions.Protocol):
            def __call__(self, __v: float, __values: SinglyLinkedListNodeValue.Partial) -> float:
                ...

        class NextValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[NodeId], __values: SinglyLinkedListNodeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: SinglyLinkedListNodeValue.Partial) -> SinglyLinkedListNodeValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: SinglyLinkedListNodeValue.Partial) -> SinglyLinkedListNodeValue.Partial:
        for validator in SinglyLinkedListNodeValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: SinglyLinkedListNodeValue.Partial) -> SinglyLinkedListNodeValue.Partial:
        for validator in SinglyLinkedListNodeValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id", pre=True)
    def _pre_validate_node_id(cls, v: NodeId, values: SinglyLinkedListNodeValue.Partial) -> NodeId:
        for validator in SinglyLinkedListNodeValue.Validators._node_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("node_id", pre=False)
    def _post_validate_node_id(cls, v: NodeId, values: SinglyLinkedListNodeValue.Partial) -> NodeId:
        for validator in SinglyLinkedListNodeValue.Validators._node_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("val", pre=True)
    def _pre_validate_val(cls, v: float, values: SinglyLinkedListNodeValue.Partial) -> float:
        for validator in SinglyLinkedListNodeValue.Validators._val_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("val", pre=False)
    def _post_validate_val(cls, v: float, values: SinglyLinkedListNodeValue.Partial) -> float:
        for validator in SinglyLinkedListNodeValue.Validators._val_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("next", pre=True)
    def _pre_validate_next(
        cls, v: typing.Optional[NodeId], values: SinglyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in SinglyLinkedListNodeValue.Validators._next_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("next", pre=False)
    def _post_validate_next(
        cls, v: typing.Optional[NodeId], values: SinglyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in SinglyLinkedListNodeValue.Validators._next_post_validators:
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
