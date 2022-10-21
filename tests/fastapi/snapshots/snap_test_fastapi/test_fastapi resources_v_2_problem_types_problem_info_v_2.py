# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.types.language import Language
from ....commons.types.problem_id import ProblemId
from ....problem.types.problem_description import ProblemDescription
from .custom_files import CustomFiles
from .generated_files import GeneratedFiles
from .test_case_template import TestCaseTemplate
from .test_case_v_2 import TestCaseV2


class ProblemInfoV2(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_description: ProblemDescription = pydantic.Field(alias="problemDescription")
    problem_name: str = pydantic.Field(alias="problemName")
    problem_version: int = pydantic.Field(alias="problemVersion")
    supported_languages: typing.List[Language] = pydantic.Field(alias="supportedLanguages")
    custom_files: CustomFiles = pydantic.Field(alias="customFiles")
    generated_files: GeneratedFiles = pydantic.Field(alias="generatedFiles")
    custom_test_case_templates: typing.List[TestCaseTemplate] = pydantic.Field(alias="customTestCaseTemplates")
    testcases: typing.List[TestCaseV2]
    is_public: bool = pydantic.Field(alias="isPublic")

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_description: typing_extensions.NotRequired[ProblemDescription]
        problem_name: typing_extensions.NotRequired[str]
        problem_version: typing_extensions.NotRequired[int]
        supported_languages: typing_extensions.NotRequired[typing.List[Language]]
        custom_files: typing_extensions.NotRequired[CustomFiles]
        generated_files: typing_extensions.NotRequired[GeneratedFiles]
        custom_test_case_templates: typing_extensions.NotRequired[typing.List[TestCaseTemplate]]
        testcases: typing_extensions.NotRequired[typing.List[TestCaseV2]]
        is_public: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ProblemInfoV2.Validators.root
            def validate(values: ProblemInfoV2.Partial) -> ProblemInfoV2.Partial:
                ...

            @ProblemInfoV2.Validators.field("problem_id")
            def validate_problem_id(v: ProblemId, values: ProblemInfoV2.Partial) -> ProblemId:
                ...

            @ProblemInfoV2.Validators.field("problem_description")
            def validate_problem_description(v: ProblemDescription, values: ProblemInfoV2.Partial) -> ProblemDescription:
                ...

            @ProblemInfoV2.Validators.field("problem_name")
            def validate_problem_name(v: str, values: ProblemInfoV2.Partial) -> str:
                ...

            @ProblemInfoV2.Validators.field("problem_version")
            def validate_problem_version(v: int, values: ProblemInfoV2.Partial) -> int:
                ...

            @ProblemInfoV2.Validators.field("supported_languages")
            def validate_supported_languages(v: typing.List[Language], values: ProblemInfoV2.Partial) -> typing.List[Language]:
                ...

            @ProblemInfoV2.Validators.field("custom_files")
            def validate_custom_files(v: CustomFiles, values: ProblemInfoV2.Partial) -> CustomFiles:
                ...

            @ProblemInfoV2.Validators.field("generated_files")
            def validate_generated_files(v: GeneratedFiles, values: ProblemInfoV2.Partial) -> GeneratedFiles:
                ...

            @ProblemInfoV2.Validators.field("custom_test_case_templates")
            def validate_custom_test_case_templates(v: typing.List[TestCaseTemplate], values: ProblemInfoV2.Partial) -> typing.List[TestCaseTemplate]:
                ...

            @ProblemInfoV2.Validators.field("testcases")
            def validate_testcases(v: typing.List[TestCaseV2], values: ProblemInfoV2.Partial) -> typing.List[TestCaseV2]:
                ...

            @ProblemInfoV2.Validators.field("is_public")
            def validate_is_public(v: bool, values: ProblemInfoV2.Partial) -> bool:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[ProblemInfoV2.Partial], ProblemInfoV2.Partial]]] = []
        _problem_id_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.ProblemIdValidator]] = []
        _problem_description_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.ProblemDescriptionValidator]
        ] = []
        _problem_name_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.ProblemNameValidator]] = []
        _problem_version_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.ProblemVersionValidator]] = []
        _supported_languages_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.SupportedLanguagesValidator]
        ] = []
        _custom_files_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.CustomFilesValidator]] = []
        _generated_files_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.GeneratedFilesValidator]] = []
        _custom_test_case_templates_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.CustomTestCaseTemplatesValidator]
        ] = []
        _testcases_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.TestcasesValidator]] = []
        _is_public_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.IsPublicValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[ProblemInfoV2.Partial], ProblemInfoV2.Partial]
        ) -> typing.Callable[[ProblemInfoV2.Partial], ProblemInfoV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemIdValidator], ProblemInfoV2.Validators.ProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_description"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemDescriptionValidator], ProblemInfoV2.Validators.ProblemDescriptionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemNameValidator], ProblemInfoV2.Validators.ProblemNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemVersionValidator], ProblemInfoV2.Validators.ProblemVersionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["supported_languages"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.SupportedLanguagesValidator], ProblemInfoV2.Validators.SupportedLanguagesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_files"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.CustomFilesValidator], ProblemInfoV2.Validators.CustomFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["generated_files"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.GeneratedFilesValidator], ProblemInfoV2.Validators.GeneratedFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_test_case_templates"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.CustomTestCaseTemplatesValidator],
            ProblemInfoV2.Validators.CustomTestCaseTemplatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.TestcasesValidator], ProblemInfoV2.Validators.TestcasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_public"]
        ) -> typing.Callable[[ProblemInfoV2.Validators.IsPublicValidator], ProblemInfoV2.Validators.IsPublicValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                if field_name == "problem_description":
                    cls._problem_description_validators.append(validator)
                if field_name == "problem_name":
                    cls._problem_name_validators.append(validator)
                if field_name == "problem_version":
                    cls._problem_version_validators.append(validator)
                if field_name == "supported_languages":
                    cls._supported_languages_validators.append(validator)
                if field_name == "custom_files":
                    cls._custom_files_validators.append(validator)
                if field_name == "generated_files":
                    cls._generated_files_validators.append(validator)
                if field_name == "custom_test_case_templates":
                    cls._custom_test_case_templates_validators.append(validator)
                if field_name == "testcases":
                    cls._testcases_validators.append(validator)
                if field_name == "is_public":
                    cls._is_public_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, v: ProblemId, *, values: ProblemInfoV2.Partial) -> ProblemId:
                ...

        class ProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, v: ProblemDescription, *, values: ProblemInfoV2.Partial) -> ProblemDescription:
                ...

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: ProblemInfoV2.Partial) -> str:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, v: int, *, values: ProblemInfoV2.Partial) -> int:
                ...

        class SupportedLanguagesValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.List[Language], *, values: ProblemInfoV2.Partial) -> typing.List[Language]:
                ...

        class CustomFilesValidator(typing_extensions.Protocol):
            def __call__(self, v: CustomFiles, *, values: ProblemInfoV2.Partial) -> CustomFiles:
                ...

        class GeneratedFilesValidator(typing_extensions.Protocol):
            def __call__(self, v: GeneratedFiles, *, values: ProblemInfoV2.Partial) -> GeneratedFiles:
                ...

        class CustomTestCaseTemplatesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TestCaseTemplate], *, values: ProblemInfoV2.Partial
            ) -> typing.List[TestCaseTemplate]:
                ...

        class TestcasesValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.List[TestCaseV2], *, values: ProblemInfoV2.Partial) -> typing.List[TestCaseV2]:
                ...

        class IsPublicValidator(typing_extensions.Protocol):
            def __call__(self, v: bool, *, values: ProblemInfoV2.Partial) -> bool:
                ...

    @pydantic.root_validator
    def _validate(cls, values: ProblemInfoV2.Partial) -> ProblemInfoV2.Partial:
        for validator in ProblemInfoV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, v: ProblemId, values: ProblemInfoV2.Partial) -> ProblemId:
        for validator in ProblemInfoV2.Validators._problem_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_description")
    def _validate_problem_description(cls, v: ProblemDescription, values: ProblemInfoV2.Partial) -> ProblemDescription:
        for validator in ProblemInfoV2.Validators._problem_description_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_name")
    def _validate_problem_name(cls, v: str, values: ProblemInfoV2.Partial) -> str:
        for validator in ProblemInfoV2.Validators._problem_name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_version")
    def _validate_problem_version(cls, v: int, values: ProblemInfoV2.Partial) -> int:
        for validator in ProblemInfoV2.Validators._problem_version_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("supported_languages")
    def _validate_supported_languages(
        cls, v: typing.List[Language], values: ProblemInfoV2.Partial
    ) -> typing.List[Language]:
        for validator in ProblemInfoV2.Validators._supported_languages_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("custom_files")
    def _validate_custom_files(cls, v: CustomFiles, values: ProblemInfoV2.Partial) -> CustomFiles:
        for validator in ProblemInfoV2.Validators._custom_files_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("generated_files")
    def _validate_generated_files(cls, v: GeneratedFiles, values: ProblemInfoV2.Partial) -> GeneratedFiles:
        for validator in ProblemInfoV2.Validators._generated_files_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("custom_test_case_templates")
    def _validate_custom_test_case_templates(
        cls, v: typing.List[TestCaseTemplate], values: ProblemInfoV2.Partial
    ) -> typing.List[TestCaseTemplate]:
        for validator in ProblemInfoV2.Validators._custom_test_case_templates_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("testcases")
    def _validate_testcases(cls, v: typing.List[TestCaseV2], values: ProblemInfoV2.Partial) -> typing.List[TestCaseV2]:
        for validator in ProblemInfoV2.Validators._testcases_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("is_public")
    def _validate_is_public(cls, v: bool, values: ProblemInfoV2.Partial) -> bool:
        for validator in ProblemInfoV2.Validators._is_public_validators:
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
