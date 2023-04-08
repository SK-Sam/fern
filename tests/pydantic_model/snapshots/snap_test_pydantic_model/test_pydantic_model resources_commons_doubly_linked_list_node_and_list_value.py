# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .doubly_linked_list_value import DoublyLinkedListValue
from .node_id import NodeId


class DoublyLinkedListNodeAndListValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_list: DoublyLinkedListValue = pydantic.Field(alias="fullList")

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        full_list: typing_extensions.NotRequired[DoublyLinkedListValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DoublyLinkedListNodeAndListValue.Validators.root()
            def validate(values: DoublyLinkedListNodeAndListValue.Partial) -> DoublyLinkedListNodeAndListValue.Partial:
                ...

            @DoublyLinkedListNodeAndListValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: DoublyLinkedListNodeAndListValue.Partial) -> NodeId:
                ...

            @DoublyLinkedListNodeAndListValue.Validators.field("full_list")
            def validate_full_list(full_list: DoublyLinkedListValue, values: DoublyLinkedListNodeAndListValue.Partial) -> DoublyLinkedListValue:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[DoublyLinkedListNodeAndListValue.Validators._PreRootValidator]
        ] = []
        _post_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeAndListValue.Validators._RootValidator]] = []
        _node_id_pre_validators: typing.ClassVar[
            typing.List[DoublyLinkedListNodeAndListValue.Validators.PreNodeIdValidator]
        ] = []
        _node_id_post_validators: typing.ClassVar[
            typing.List[DoublyLinkedListNodeAndListValue.Validators.NodeIdValidator]
        ] = []
        _full_list_pre_validators: typing.ClassVar[
            typing.List[DoublyLinkedListNodeAndListValue.Validators.PreFullListValidator]
        ] = []
        _full_list_post_validators: typing.ClassVar[
            typing.List[DoublyLinkedListNodeAndListValue.Validators.FullListValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DoublyLinkedListNodeAndListValue.Validators._RootValidator],
            DoublyLinkedListNodeAndListValue.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DoublyLinkedListNodeAndListValue.Validators._PreRootValidator],
            DoublyLinkedListNodeAndListValue.Validators._PreRootValidator,
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
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
            cls, field_name: typing_extensions.Literal["node_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DoublyLinkedListNodeAndListValue.Validators.PreNodeIdValidator],
            DoublyLinkedListNodeAndListValue.Validators.PreNodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DoublyLinkedListNodeAndListValue.Validators.NodeIdValidator],
            DoublyLinkedListNodeAndListValue.Validators.NodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_list"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DoublyLinkedListNodeAndListValue.Validators.PreFullListValidator],
            DoublyLinkedListNodeAndListValue.Validators.PreFullListValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_list"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DoublyLinkedListNodeAndListValue.Validators.FullListValidator],
            DoublyLinkedListNodeAndListValue.Validators.FullListValidator,
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
                if field_name == "full_list":
                    if pre:
                        cls._full_list_pre_validators.append(validator)
                    else:
                        cls._full_list_post_validators.append(validator)
                return validator

            return decorator

        class PreNodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DoublyLinkedListNodeAndListValue.Partial) -> typing.Any:
                ...

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: NodeId, __values: DoublyLinkedListNodeAndListValue.Partial) -> NodeId:
                ...

        class PreFullListValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DoublyLinkedListNodeAndListValue.Partial) -> typing.Any:
                ...

        class FullListValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: DoublyLinkedListValue, __values: DoublyLinkedListNodeAndListValue.Partial
            ) -> DoublyLinkedListValue:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: DoublyLinkedListNodeAndListValue.Partial
            ) -> DoublyLinkedListNodeAndListValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: DoublyLinkedListNodeAndListValue.Partial
    ) -> DoublyLinkedListNodeAndListValue.Partial:
        for validator in DoublyLinkedListNodeAndListValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: DoublyLinkedListNodeAndListValue.Partial
    ) -> DoublyLinkedListNodeAndListValue.Partial:
        for validator in DoublyLinkedListNodeAndListValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id", pre=True)
    def _pre_validate_node_id(cls, v: NodeId, values: DoublyLinkedListNodeAndListValue.Partial) -> NodeId:
        for validator in DoublyLinkedListNodeAndListValue.Validators._node_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("node_id", pre=False)
    def _post_validate_node_id(cls, v: NodeId, values: DoublyLinkedListNodeAndListValue.Partial) -> NodeId:
        for validator in DoublyLinkedListNodeAndListValue.Validators._node_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("full_list", pre=True)
    def _pre_validate_full_list(
        cls, v: DoublyLinkedListValue, values: DoublyLinkedListNodeAndListValue.Partial
    ) -> DoublyLinkedListValue:
        for validator in DoublyLinkedListNodeAndListValue.Validators._full_list_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("full_list", pre=False)
    def _post_validate_full_list(
        cls, v: DoublyLinkedListValue, values: DoublyLinkedListNodeAndListValue.Partial
    ) -> DoublyLinkedListValue:
        for validator in DoublyLinkedListNodeAndListValue.Validators._full_list_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
