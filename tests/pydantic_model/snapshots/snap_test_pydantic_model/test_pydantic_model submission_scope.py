# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.debug_variable_value import DebugVariableValue


class Scope(pydantic.BaseModel):
    variables: typing.Dict[str, DebugVariableValue]

    class Partial(typing_extensions.TypedDict):
        variables: typing_extensions.NotRequired[typing.Dict[str, DebugVariableValue]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Scope.Validators.root
            def validate(values: Scope.Partial) -> Scope.Partial:
                ...

            @Scope.Validators.field("variables")
            def validate_variables(v: typing.Dict[str, DebugVariableValue], values: Scope.Partial) -> typing.Dict[str, DebugVariableValue]:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[Scope.Partial], Scope.Partial]]] = []
        _variables_validators: typing.ClassVar[typing.List[Scope.Validators.VariablesValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[Scope.Partial], Scope.Partial]
        ) -> typing.Callable[[Scope.Partial], Scope.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variables"]
        ) -> typing.Callable[[Scope.Validators.VariablesValidator], Scope.Validators.VariablesValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "variables":
                    cls._variables_validators.append(validator)
                return validator

            return decorator

        class VariablesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[str, DebugVariableValue], *, values: Scope.Partial
            ) -> typing.Dict[str, DebugVariableValue]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: Scope.Partial) -> Scope.Partial:
        for validator in Scope.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("variables")
    def _validate_variables(
        cls, v: typing.Dict[str, DebugVariableValue], values: Scope.Partial
    ) -> typing.Dict[str, DebugVariableValue]:
        for validator in Scope.Validators._variables_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
