# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.variable_type import VariableType
from .parameter_id import ParameterId


class Parameter(pydantic.BaseModel):
    parameter_id: ParameterId = pydantic.Field(alias="parameterId")
    name: str
    variable_type: VariableType = pydantic.Field(alias="variableType")

    class Partial(typing_extensions.TypedDict):
        parameter_id: typing_extensions.NotRequired[ParameterId]
        name: typing_extensions.NotRequired[str]
        variable_type: typing_extensions.NotRequired[VariableType]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Parameter.Validators.root
            def validate(values: Parameter.Partial) -> Parameter.Partial:
                ...

            @Parameter.Validators.field("parameter_id")
            def validate_parameter_id(v: ParameterId, values: Parameter.Partial) -> ParameterId:
                ...

            @Parameter.Validators.field("name")
            def validate_name(v: str, values: Parameter.Partial) -> str:
                ...

            @Parameter.Validators.field("variable_type")
            def validate_variable_type(v: VariableType, values: Parameter.Partial) -> VariableType:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[Parameter.Partial], Parameter.Partial]]] = []
        _parameter_id_validators: typing.ClassVar[typing.List[Parameter.Validators.ParameterIdValidator]] = []
        _name_validators: typing.ClassVar[typing.List[Parameter.Validators.NameValidator]] = []
        _variable_type_validators: typing.ClassVar[typing.List[Parameter.Validators.VariableTypeValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[Parameter.Partial], Parameter.Partial]
        ) -> typing.Callable[[Parameter.Partial], Parameter.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["parameter_id"]
        ) -> typing.Callable[[Parameter.Validators.ParameterIdValidator], Parameter.Validators.ParameterIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[[Parameter.Validators.NameValidator], Parameter.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variable_type"]
        ) -> typing.Callable[[Parameter.Validators.VariableTypeValidator], Parameter.Validators.VariableTypeValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameter_id":
                    cls._parameter_id_validators.append(validator)
                if field_name == "name":
                    cls._name_validators.append(validator)
                if field_name == "variable_type":
                    cls._variable_type_validators.append(validator)
                return validator

            return decorator

        class ParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, v: ParameterId, *, values: Parameter.Partial) -> ParameterId:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: Parameter.Partial) -> str:
                ...

        class VariableTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: Parameter.Partial) -> VariableType:
                ...

    @pydantic.root_validator
    def _validate(cls, values: Parameter.Partial) -> Parameter.Partial:
        for validator in Parameter.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("parameter_id")
    def _validate_parameter_id(cls, v: ParameterId, values: Parameter.Partial) -> ParameterId:
        for validator in Parameter.Validators._parameter_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("name")
    def _validate_name(cls, v: str, values: Parameter.Partial) -> str:
        for validator in Parameter.Validators._name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("variable_type")
    def _validate_variable_type(cls, v: VariableType, values: Parameter.Partial) -> VariableType:
        for validator in Parameter.Validators._variable_type_validators:
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
        allow_population_by_field_name = True
