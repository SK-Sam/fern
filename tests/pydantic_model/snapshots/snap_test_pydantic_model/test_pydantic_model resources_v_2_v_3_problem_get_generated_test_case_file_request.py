# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .....core.datetime_utils import serialize_datetime
from .test_case_template import TestCaseTemplate
from .test_case_v_2 import TestCaseV2


class GetGeneratedTestCaseFileRequest(pydantic.BaseModel):
    template: typing.Optional[TestCaseTemplate]
    test_case: TestCaseV2 = pydantic.Field(alias="testCase")

    class Partial(typing_extensions.TypedDict):
        template: typing_extensions.NotRequired[typing.Optional[TestCaseTemplate]]
        test_case: typing_extensions.NotRequired[TestCaseV2]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetGeneratedTestCaseFileRequest.Validators.root()
            def validate(values: GetGeneratedTestCaseFileRequest.Partial) -> GetGeneratedTestCaseFileRequest.Partial:
                ...

            @GetGeneratedTestCaseFileRequest.Validators.field("template")
            def validate_template(template: typing.Optional[TestCaseTemplate], values: GetGeneratedTestCaseFileRequest.Partial) -> typing.Optional[TestCaseTemplate]:
                ...

            @GetGeneratedTestCaseFileRequest.Validators.field("test_case")
            def validate_test_case(test_case: TestCaseV2, values: GetGeneratedTestCaseFileRequest.Partial) -> TestCaseV2:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GetGeneratedTestCaseFileRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GetGeneratedTestCaseFileRequest.Validators._RootValidator]] = []
        _template_pre_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseFileRequest.Validators.PreTemplateValidator]
        ] = []
        _template_post_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseFileRequest.Validators.TemplateValidator]
        ] = []
        _test_case_pre_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseFileRequest.Validators.PreTestCaseValidator]
        ] = []
        _test_case_post_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseFileRequest.Validators.TestCaseValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators._RootValidator],
            GetGeneratedTestCaseFileRequest.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators._PreRootValidator],
            GetGeneratedTestCaseFileRequest.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["template"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators.PreTemplateValidator],
            GetGeneratedTestCaseFileRequest.Validators.PreTemplateValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators.TemplateValidator],
            GetGeneratedTestCaseFileRequest.Validators.TemplateValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators.PreTestCaseValidator],
            GetGeneratedTestCaseFileRequest.Validators.PreTestCaseValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators.TestCaseValidator],
            GetGeneratedTestCaseFileRequest.Validators.TestCaseValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template":
                    if pre:
                        cls._template_pre_validators.append(validator)
                    else:
                        cls._template_post_validators.append(validator)
                if field_name == "test_case":
                    if pre:
                        cls._test_case_pre_validators.append(validator)
                    else:
                        cls._test_case_post_validators.append(validator)
                return validator

            return decorator

        class PreTemplateValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetGeneratedTestCaseFileRequest.Partial) -> typing.Any:
                ...

        class TemplateValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[TestCaseTemplate], __values: GetGeneratedTestCaseFileRequest.Partial
            ) -> typing.Optional[TestCaseTemplate]:
                ...

        class PreTestCaseValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetGeneratedTestCaseFileRequest.Partial) -> typing.Any:
                ...

        class TestCaseValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseV2, __values: GetGeneratedTestCaseFileRequest.Partial) -> TestCaseV2:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: GetGeneratedTestCaseFileRequest.Partial
            ) -> GetGeneratedTestCaseFileRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: GetGeneratedTestCaseFileRequest.Partial) -> GetGeneratedTestCaseFileRequest.Partial:
        for validator in GetGeneratedTestCaseFileRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: GetGeneratedTestCaseFileRequest.Partial) -> GetGeneratedTestCaseFileRequest.Partial:
        for validator in GetGeneratedTestCaseFileRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("template", pre=True)
    def _pre_validate_template(
        cls, v: typing.Optional[TestCaseTemplate], values: GetGeneratedTestCaseFileRequest.Partial
    ) -> typing.Optional[TestCaseTemplate]:
        for validator in GetGeneratedTestCaseFileRequest.Validators._template_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("template", pre=False)
    def _post_validate_template(
        cls, v: typing.Optional[TestCaseTemplate], values: GetGeneratedTestCaseFileRequest.Partial
    ) -> typing.Optional[TestCaseTemplate]:
        for validator in GetGeneratedTestCaseFileRequest.Validators._template_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case", pre=True)
    def _pre_validate_test_case(cls, v: TestCaseV2, values: GetGeneratedTestCaseFileRequest.Partial) -> TestCaseV2:
        for validator in GetGeneratedTestCaseFileRequest.Validators._test_case_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case", pre=False)
    def _post_validate_test_case(cls, v: TestCaseV2, values: GetGeneratedTestCaseFileRequest.Partial) -> TestCaseV2:
        for validator in GetGeneratedTestCaseFileRequest.Validators._test_case_post_validators:
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
