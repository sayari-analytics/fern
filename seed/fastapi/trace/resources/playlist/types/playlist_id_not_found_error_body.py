# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .playlist_id import PlaylistId as resources_playlist_types_playlist_id_PlaylistId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def playlist_id(self, value: resources_playlist_types_playlist_id_PlaylistId) -> PlaylistIdNotFoundErrorBody:
        return PlaylistIdNotFoundErrorBody(
            __root__=_PlaylistIdNotFoundErrorBody.PlaylistId(type="playlistId", value=value)
        )


class PlaylistIdNotFoundErrorBody(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId]:
        return self.__root__

    def visit(
        self, playlist_id: typing.Callable[[resources_playlist_types_playlist_id_PlaylistId], T_Result]
    ) -> T_Result:
        if self.__root__.type == "playlistId":
            return playlist_id(self.__root__.value)

    __root__: typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _PlaylistIdNotFoundErrorBody:
    class PlaylistId(pydantic.BaseModel):
        type: typing.Literal["playlistId"]
        value: resources_playlist_types_playlist_id_PlaylistId


PlaylistIdNotFoundErrorBody.update_forward_refs()
