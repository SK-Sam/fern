# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .execution_session_status import ExecutionSessionStatus
from .submission_id import SubmissionId


class BuildingExecutorResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    status: ExecutionSessionStatus

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        status: typing_extensions.NotRequired[ExecutionSessionStatus]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BuildingExecutorResponse.Validators.root()
            def validate(values: BuildingExecutorResponse.Partial) -> BuildingExecutorResponse.Partial:
                ...

            @BuildingExecutorResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: BuildingExecutorResponse.Partial) -> SubmissionId:
                ...

            @BuildingExecutorResponse.Validators.field("status")
            def validate_status(status: ExecutionSessionStatus, values: BuildingExecutorResponse.Partial) -> ExecutionSessionStatus:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[BuildingExecutorResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[BuildingExecutorResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[BuildingExecutorResponse.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[BuildingExecutorResponse.Validators.SubmissionIdValidator]
        ] = []
        _status_pre_validators: typing.ClassVar[
            typing.List[BuildingExecutorResponse.Validators.PreStatusValidator]
        ] = []
        _status_post_validators: typing.ClassVar[typing.List[BuildingExecutorResponse.Validators.StatusValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BuildingExecutorResponse.Validators._RootValidator], BuildingExecutorResponse.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BuildingExecutorResponse.Validators._PreRootValidator],
            BuildingExecutorResponse.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BuildingExecutorResponse.Validators.PreSubmissionIdValidator],
            BuildingExecutorResponse.Validators.PreSubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [BuildingExecutorResponse.Validators.SubmissionIdValidator],
            BuildingExecutorResponse.Validators.SubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BuildingExecutorResponse.Validators.PreStatusValidator],
            BuildingExecutorResponse.Validators.PreStatusValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BuildingExecutorResponse.Validators.StatusValidator], BuildingExecutorResponse.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "status":
                    if pre:
                        cls._status_pre_validators.append(validator)
                    else:
                        cls._status_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BuildingExecutorResponse.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: BuildingExecutorResponse.Partial) -> SubmissionId:
                ...

        class PreStatusValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BuildingExecutorResponse.Partial) -> typing.Any:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: ExecutionSessionStatus, __values: BuildingExecutorResponse.Partial
            ) -> ExecutionSessionStatus:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: BuildingExecutorResponse.Partial) -> BuildingExecutorResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: BuildingExecutorResponse.Partial) -> BuildingExecutorResponse.Partial:
        for validator in BuildingExecutorResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: BuildingExecutorResponse.Partial) -> BuildingExecutorResponse.Partial:
        for validator in BuildingExecutorResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: BuildingExecutorResponse.Partial) -> SubmissionId:
        for validator in BuildingExecutorResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: BuildingExecutorResponse.Partial) -> SubmissionId:
        for validator in BuildingExecutorResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=True)
    def _pre_validate_status(
        cls, v: ExecutionSessionStatus, values: BuildingExecutorResponse.Partial
    ) -> ExecutionSessionStatus:
        for validator in BuildingExecutorResponse.Validators._status_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=False)
    def _post_validate_status(
        cls, v: ExecutionSessionStatus, values: BuildingExecutorResponse.Partial
    ) -> ExecutionSessionStatus:
        for validator in BuildingExecutorResponse.Validators._status_post_validators:
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
