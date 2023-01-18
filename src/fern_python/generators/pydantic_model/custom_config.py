import pydantic


class PydanticModelCustomConfig(pydantic.BaseModel):
    include_validators: bool = False
    forbid_extra_fields: bool = False
    wrapped_aliases: bool = False
