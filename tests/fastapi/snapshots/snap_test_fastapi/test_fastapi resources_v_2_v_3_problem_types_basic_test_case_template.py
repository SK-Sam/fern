# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .parameter_id import ParameterId
from .test_case_implementation_description import TestCaseImplementationDescription
from .test_case_template_id import TestCaseTemplateId


class BasicTestCaseTemplate(pydantic.BaseModel):
    template_id: TestCaseTemplateId = pydantic.Field(alias="templateId")
    name: str
    description: TestCaseImplementationDescription
    expected_value_parameter_id: ParameterId = pydantic.Field(alias="expectedValueParameterId")

    class Partial(typing_extensions.TypedDict):
        template_id: typing_extensions.NotRequired[TestCaseTemplateId]
        name: typing_extensions.NotRequired[str]
        description: typing_extensions.NotRequired[TestCaseImplementationDescription]
        expected_value_parameter_id: typing_extensions.NotRequired[ParameterId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BasicTestCaseTemplate.Validators.root
            def validate(values: BasicTestCaseTemplate.Partial) -> BasicTestCaseTemplate.Partial:
                ...

            @BasicTestCaseTemplate.Validators.field("template_id")
            def validate_template_id(v: TestCaseTemplateId, values: BasicTestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

            @BasicTestCaseTemplate.Validators.field("name")
            def validate_name(v: str, values: BasicTestCaseTemplate.Partial) -> str:
                ...

            @BasicTestCaseTemplate.Validators.field("description")
            def validate_description(v: TestCaseImplementationDescription, values: BasicTestCaseTemplate.Partial) -> TestCaseImplementationDescription:
                ...

            @BasicTestCaseTemplate.Validators.field("expected_value_parameter_id")
            def validate_expected_value_parameter_id(v: ParameterId, values: BasicTestCaseTemplate.Partial) -> ParameterId:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[BasicTestCaseTemplate.Partial], BasicTestCaseTemplate.Partial]]
        ] = []
        _template_id_validators: typing.ClassVar[typing.List[BasicTestCaseTemplate.Validators.TemplateIdValidator]] = []
        _name_validators: typing.ClassVar[typing.List[BasicTestCaseTemplate.Validators.NameValidator]] = []
        _description_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.DescriptionValidator]
        ] = []
        _expected_value_parameter_id_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.ExpectedValueParameterIdValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[BasicTestCaseTemplate.Partial], BasicTestCaseTemplate.Partial]
        ) -> typing.Callable[[BasicTestCaseTemplate.Partial], BasicTestCaseTemplate.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template_id"]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.TemplateIdValidator], BasicTestCaseTemplate.Validators.TemplateIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.NameValidator], BasicTestCaseTemplate.Validators.NameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["description"]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.DescriptionValidator],
            BasicTestCaseTemplate.Validators.DescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_value_parameter_id"]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.ExpectedValueParameterIdValidator],
            BasicTestCaseTemplate.Validators.ExpectedValueParameterIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template_id":
                    cls._template_id_validators.append(validator)
                if field_name == "name":
                    cls._name_validators.append(validator)
                if field_name == "description":
                    cls._description_validators.append(validator)
                if field_name == "expected_value_parameter_id":
                    cls._expected_value_parameter_id_validators.append(validator)
                return validator

            return decorator

        class TemplateIdValidator(typing_extensions.Protocol):
            def __call__(self, v: TestCaseTemplateId, *, values: BasicTestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: BasicTestCaseTemplate.Partial) -> str:
                ...

        class DescriptionValidator(typing_extensions.Protocol):
            def __call__(
                self, v: TestCaseImplementationDescription, *, values: BasicTestCaseTemplate.Partial
            ) -> TestCaseImplementationDescription:
                ...

        class ExpectedValueParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, v: ParameterId, *, values: BasicTestCaseTemplate.Partial) -> ParameterId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: BasicTestCaseTemplate.Partial) -> BasicTestCaseTemplate.Partial:
        for validator in BasicTestCaseTemplate.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("template_id")
    def _validate_template_id(cls, v: TestCaseTemplateId, values: BasicTestCaseTemplate.Partial) -> TestCaseTemplateId:
        for validator in BasicTestCaseTemplate.Validators._template_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("name")
    def _validate_name(cls, v: str, values: BasicTestCaseTemplate.Partial) -> str:
        for validator in BasicTestCaseTemplate.Validators._name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("description")
    def _validate_description(
        cls, v: TestCaseImplementationDescription, values: BasicTestCaseTemplate.Partial
    ) -> TestCaseImplementationDescription:
        for validator in BasicTestCaseTemplate.Validators._description_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("expected_value_parameter_id")
    def _validate_expected_value_parameter_id(
        cls, v: ParameterId, values: BasicTestCaseTemplate.Partial
    ) -> ParameterId:
        for validator in BasicTestCaseTemplate.Validators._expected_value_parameter_id_validators:
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
