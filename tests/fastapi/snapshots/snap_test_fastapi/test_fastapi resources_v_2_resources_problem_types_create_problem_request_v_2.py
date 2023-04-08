# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .....commons.types.language import Language
from .....problem.types.problem_description import ProblemDescription
from .custom_files import CustomFiles
from .test_case_template import TestCaseTemplate
from .test_case_v_2 import TestCaseV2


class CreateProblemRequestV2(pydantic.BaseModel):
    problem_name: str = pydantic.Field(alias="problemName")
    problem_description: ProblemDescription = pydantic.Field(alias="problemDescription")
    custom_files: CustomFiles = pydantic.Field(alias="customFiles")
    custom_test_case_templates: typing.List[TestCaseTemplate] = pydantic.Field(alias="customTestCaseTemplates")
    testcases: typing.List[TestCaseV2]
    supported_languages: typing.List[Language] = pydantic.Field(alias="supportedLanguages")
    is_public: bool = pydantic.Field(alias="isPublic")

    class Partial(typing_extensions.TypedDict):
        problem_name: typing_extensions.NotRequired[str]
        problem_description: typing_extensions.NotRequired[ProblemDescription]
        custom_files: typing_extensions.NotRequired[CustomFiles]
        custom_test_case_templates: typing_extensions.NotRequired[typing.List[TestCaseTemplate]]
        testcases: typing_extensions.NotRequired[typing.List[TestCaseV2]]
        supported_languages: typing_extensions.NotRequired[typing.List[Language]]
        is_public: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CreateProblemRequestV2.Validators.root()
            def validate(values: CreateProblemRequestV2.Partial) -> CreateProblemRequestV2.Partial:
                ...

            @CreateProblemRequestV2.Validators.field("problem_name")
            def validate_problem_name(problem_name: str, values: CreateProblemRequestV2.Partial) -> str:
                ...

            @CreateProblemRequestV2.Validators.field("problem_description")
            def validate_problem_description(problem_description: ProblemDescription, values: CreateProblemRequestV2.Partial) -> ProblemDescription:
                ...

            @CreateProblemRequestV2.Validators.field("custom_files")
            def validate_custom_files(custom_files: CustomFiles, values: CreateProblemRequestV2.Partial) -> CustomFiles:
                ...

            @CreateProblemRequestV2.Validators.field("custom_test_case_templates")
            def validate_custom_test_case_templates(custom_test_case_templates: typing.List[TestCaseTemplate], values: CreateProblemRequestV2.Partial) -> typing.List[TestCaseTemplate]:
                ...

            @CreateProblemRequestV2.Validators.field("testcases")
            def validate_testcases(testcases: typing.List[TestCaseV2], values: CreateProblemRequestV2.Partial) -> typing.List[TestCaseV2]:
                ...

            @CreateProblemRequestV2.Validators.field("supported_languages")
            def validate_supported_languages(supported_languages: typing.List[Language], values: CreateProblemRequestV2.Partial) -> typing.List[Language]:
                ...

            @CreateProblemRequestV2.Validators.field("is_public")
            def validate_is_public(is_public: bool, values: CreateProblemRequestV2.Partial) -> bool:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[CreateProblemRequestV2.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[CreateProblemRequestV2.Validators._RootValidator]] = []
        _problem_name_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.PreProblemNameValidator]
        ] = []
        _problem_name_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.ProblemNameValidator]
        ] = []
        _problem_description_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.PreProblemDescriptionValidator]
        ] = []
        _problem_description_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.ProblemDescriptionValidator]
        ] = []
        _custom_files_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.PreCustomFilesValidator]
        ] = []
        _custom_files_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.CustomFilesValidator]
        ] = []
        _custom_test_case_templates_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.PreCustomTestCaseTemplatesValidator]
        ] = []
        _custom_test_case_templates_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.CustomTestCaseTemplatesValidator]
        ] = []
        _testcases_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.PreTestcasesValidator]
        ] = []
        _testcases_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.TestcasesValidator]
        ] = []
        _supported_languages_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.PreSupportedLanguagesValidator]
        ] = []
        _supported_languages_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.SupportedLanguagesValidator]
        ] = []
        _is_public_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.PreIsPublicValidator]
        ] = []
        _is_public_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.IsPublicValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators._RootValidator], CreateProblemRequestV2.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators._PreRootValidator], CreateProblemRequestV2.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["problem_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.PreProblemNameValidator],
            CreateProblemRequestV2.Validators.PreProblemNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.ProblemNameValidator],
            CreateProblemRequestV2.Validators.ProblemNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_description"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.PreProblemDescriptionValidator],
            CreateProblemRequestV2.Validators.PreProblemDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["problem_description"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.ProblemDescriptionValidator],
            CreateProblemRequestV2.Validators.ProblemDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.PreCustomFilesValidator],
            CreateProblemRequestV2.Validators.PreCustomFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_files"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.CustomFilesValidator],
            CreateProblemRequestV2.Validators.CustomFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["custom_test_case_templates"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.PreCustomTestCaseTemplatesValidator],
            CreateProblemRequestV2.Validators.PreCustomTestCaseTemplatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["custom_test_case_templates"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.CustomTestCaseTemplatesValidator],
            CreateProblemRequestV2.Validators.CustomTestCaseTemplatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.PreTestcasesValidator],
            CreateProblemRequestV2.Validators.PreTestcasesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.TestcasesValidator], CreateProblemRequestV2.Validators.TestcasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["supported_languages"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.PreSupportedLanguagesValidator],
            CreateProblemRequestV2.Validators.PreSupportedLanguagesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["supported_languages"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.SupportedLanguagesValidator],
            CreateProblemRequestV2.Validators.SupportedLanguagesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_public"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.PreIsPublicValidator],
            CreateProblemRequestV2.Validators.PreIsPublicValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_public"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.IsPublicValidator], CreateProblemRequestV2.Validators.IsPublicValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_name":
                    if pre:
                        cls._problem_name_pre_validators.append(validator)
                    else:
                        cls._problem_name_post_validators.append(validator)
                if field_name == "problem_description":
                    if pre:
                        cls._problem_description_pre_validators.append(validator)
                    else:
                        cls._problem_description_post_validators.append(validator)
                if field_name == "custom_files":
                    if pre:
                        cls._custom_files_pre_validators.append(validator)
                    else:
                        cls._custom_files_post_validators.append(validator)
                if field_name == "custom_test_case_templates":
                    if pre:
                        cls._custom_test_case_templates_pre_validators.append(validator)
                    else:
                        cls._custom_test_case_templates_post_validators.append(validator)
                if field_name == "testcases":
                    if pre:
                        cls._testcases_pre_validators.append(validator)
                    else:
                        cls._testcases_post_validators.append(validator)
                if field_name == "supported_languages":
                    if pre:
                        cls._supported_languages_pre_validators.append(validator)
                    else:
                        cls._supported_languages_post_validators.append(validator)
                if field_name == "is_public":
                    if pre:
                        cls._is_public_pre_validators.append(validator)
                    else:
                        cls._is_public_post_validators.append(validator)
                return validator

            return decorator

        class PreProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequestV2.Partial) -> typing.Any:
                ...

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: CreateProblemRequestV2.Partial) -> str:
                ...

        class PreProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequestV2.Partial) -> typing.Any:
                ...

        class ProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemDescription, __values: CreateProblemRequestV2.Partial) -> ProblemDescription:
                ...

        class PreCustomFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequestV2.Partial) -> typing.Any:
                ...

        class CustomFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: CustomFiles, __values: CreateProblemRequestV2.Partial) -> CustomFiles:
                ...

        class PreCustomTestCaseTemplatesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequestV2.Partial) -> typing.Any:
                ...

        class CustomTestCaseTemplatesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCaseTemplate], __values: CreateProblemRequestV2.Partial
            ) -> typing.List[TestCaseTemplate]:
                ...

        class PreTestcasesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequestV2.Partial) -> typing.Any:
                ...

        class TestcasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCaseV2], __values: CreateProblemRequestV2.Partial
            ) -> typing.List[TestCaseV2]:
                ...

        class PreSupportedLanguagesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequestV2.Partial) -> typing.Any:
                ...

        class SupportedLanguagesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[Language], __values: CreateProblemRequestV2.Partial
            ) -> typing.List[Language]:
                ...

        class PreIsPublicValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequestV2.Partial) -> typing.Any:
                ...

        class IsPublicValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: CreateProblemRequestV2.Partial) -> bool:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: CreateProblemRequestV2.Partial) -> CreateProblemRequestV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: CreateProblemRequestV2.Partial) -> CreateProblemRequestV2.Partial:
        for validator in CreateProblemRequestV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: CreateProblemRequestV2.Partial) -> CreateProblemRequestV2.Partial:
        for validator in CreateProblemRequestV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_name", pre=True)
    def _pre_validate_problem_name(cls, v: str, values: CreateProblemRequestV2.Partial) -> str:
        for validator in CreateProblemRequestV2.Validators._problem_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_name", pre=False)
    def _post_validate_problem_name(cls, v: str, values: CreateProblemRequestV2.Partial) -> str:
        for validator in CreateProblemRequestV2.Validators._problem_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_description", pre=True)
    def _pre_validate_problem_description(
        cls, v: ProblemDescription, values: CreateProblemRequestV2.Partial
    ) -> ProblemDescription:
        for validator in CreateProblemRequestV2.Validators._problem_description_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_description", pre=False)
    def _post_validate_problem_description(
        cls, v: ProblemDescription, values: CreateProblemRequestV2.Partial
    ) -> ProblemDescription:
        for validator in CreateProblemRequestV2.Validators._problem_description_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_files", pre=True)
    def _pre_validate_custom_files(cls, v: CustomFiles, values: CreateProblemRequestV2.Partial) -> CustomFiles:
        for validator in CreateProblemRequestV2.Validators._custom_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_files", pre=False)
    def _post_validate_custom_files(cls, v: CustomFiles, values: CreateProblemRequestV2.Partial) -> CustomFiles:
        for validator in CreateProblemRequestV2.Validators._custom_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_test_case_templates", pre=True)
    def _pre_validate_custom_test_case_templates(
        cls, v: typing.List[TestCaseTemplate], values: CreateProblemRequestV2.Partial
    ) -> typing.List[TestCaseTemplate]:
        for validator in CreateProblemRequestV2.Validators._custom_test_case_templates_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_test_case_templates", pre=False)
    def _post_validate_custom_test_case_templates(
        cls, v: typing.List[TestCaseTemplate], values: CreateProblemRequestV2.Partial
    ) -> typing.List[TestCaseTemplate]:
        for validator in CreateProblemRequestV2.Validators._custom_test_case_templates_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("testcases", pre=True)
    def _pre_validate_testcases(
        cls, v: typing.List[TestCaseV2], values: CreateProblemRequestV2.Partial
    ) -> typing.List[TestCaseV2]:
        for validator in CreateProblemRequestV2.Validators._testcases_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("testcases", pre=False)
    def _post_validate_testcases(
        cls, v: typing.List[TestCaseV2], values: CreateProblemRequestV2.Partial
    ) -> typing.List[TestCaseV2]:
        for validator in CreateProblemRequestV2.Validators._testcases_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("supported_languages", pre=True)
    def _pre_validate_supported_languages(
        cls, v: typing.List[Language], values: CreateProblemRequestV2.Partial
    ) -> typing.List[Language]:
        for validator in CreateProblemRequestV2.Validators._supported_languages_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("supported_languages", pre=False)
    def _post_validate_supported_languages(
        cls, v: typing.List[Language], values: CreateProblemRequestV2.Partial
    ) -> typing.List[Language]:
        for validator in CreateProblemRequestV2.Validators._supported_languages_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_public", pre=True)
    def _pre_validate_is_public(cls, v: bool, values: CreateProblemRequestV2.Partial) -> bool:
        for validator in CreateProblemRequestV2.Validators._is_public_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_public", pre=False)
    def _post_validate_is_public(cls, v: bool, values: CreateProblemRequestV2.Partial) -> bool:
        for validator in CreateProblemRequestV2.Validators._is_public_post_validators:
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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
