# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .binary_tree_node_value import BinaryTreeNodeValue
from .node_id import NodeId


class BinaryTreeValue(pydantic.BaseModel):
    root: typing.Optional[NodeId]
    nodes: typing.Dict[NodeId, BinaryTreeNodeValue]

    class Partial(typing_extensions.TypedDict):
        root: typing_extensions.NotRequired[typing.Optional[NodeId]]
        nodes: typing_extensions.NotRequired[typing.Dict[NodeId, BinaryTreeNodeValue]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BinaryTreeValue.Validators.root()
            def validate(values: BinaryTreeValue.Partial) -> BinaryTreeValue.Partial:
                ...

            @BinaryTreeValue.Validators.field("root")
            def validate_root(root: typing.Optional[NodeId], values: BinaryTreeValue.Partial) -> typing.Optional[NodeId]:
                ...

            @BinaryTreeValue.Validators.field("nodes")
            def validate_nodes(nodes: typing.Dict[NodeId, BinaryTreeNodeValue], values: BinaryTreeValue.Partial) -> typing.Dict[NodeId, BinaryTreeNodeValue]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[BinaryTreeValue.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[BinaryTreeValue.Validators._RootValidator]] = []
        _root_pre_validators: typing.ClassVar[typing.List[BinaryTreeValue.Validators.PreRootValidator]] = []
        _root_post_validators: typing.ClassVar[typing.List[BinaryTreeValue.Validators.RootValidator]] = []
        _nodes_pre_validators: typing.ClassVar[typing.List[BinaryTreeValue.Validators.PreNodesValidator]] = []
        _nodes_post_validators: typing.ClassVar[typing.List[BinaryTreeValue.Validators.NodesValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[BinaryTreeValue.Validators._RootValidator], BinaryTreeValue.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BinaryTreeValue.Validators._PreRootValidator], BinaryTreeValue.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["root"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BinaryTreeValue.Validators.PreRootValidator], BinaryTreeValue.Validators.PreRootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["root"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[BinaryTreeValue.Validators.RootValidator], BinaryTreeValue.Validators.RootValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["nodes"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BinaryTreeValue.Validators.PreNodesValidator], BinaryTreeValue.Validators.PreNodesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["nodes"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[BinaryTreeValue.Validators.NodesValidator], BinaryTreeValue.Validators.NodesValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "root":
                    if pre:
                        cls._root_pre_validators.append(validator)
                    else:
                        cls._root_post_validators.append(validator)
                if field_name == "nodes":
                    if pre:
                        cls._nodes_pre_validators.append(validator)
                    else:
                        cls._nodes_post_validators.append(validator)
                return validator

            return decorator

        class PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BinaryTreeValue.Partial) -> typing.Any:
                ...

        class RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[NodeId], __values: BinaryTreeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class PreNodesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BinaryTreeValue.Partial) -> typing.Any:
                ...

        class NodesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[NodeId, BinaryTreeNodeValue], __values: BinaryTreeValue.Partial
            ) -> typing.Dict[NodeId, BinaryTreeNodeValue]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: BinaryTreeValue.Partial) -> BinaryTreeValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: BinaryTreeValue.Partial) -> BinaryTreeValue.Partial:
        for validator in BinaryTreeValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: BinaryTreeValue.Partial) -> BinaryTreeValue.Partial:
        for validator in BinaryTreeValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("root", pre=True)
    def _pre_validate_root(cls, v: typing.Optional[NodeId], values: BinaryTreeValue.Partial) -> typing.Optional[NodeId]:
        for validator in BinaryTreeValue.Validators._root_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("root", pre=False)
    def _post_validate_root(
        cls, v: typing.Optional[NodeId], values: BinaryTreeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in BinaryTreeValue.Validators._root_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("nodes", pre=True)
    def _pre_validate_nodes(
        cls, v: typing.Dict[NodeId, BinaryTreeNodeValue], values: BinaryTreeValue.Partial
    ) -> typing.Dict[NodeId, BinaryTreeNodeValue]:
        for validator in BinaryTreeValue.Validators._nodes_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("nodes", pre=False)
    def _post_validate_nodes(
        cls, v: typing.Dict[NodeId, BinaryTreeNodeValue], values: BinaryTreeValue.Partial
    ) -> typing.Dict[NodeId, BinaryTreeNodeValue]:
        for validator in BinaryTreeValue.Validators._nodes_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
