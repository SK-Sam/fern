# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .exception_info import ExceptionInfo


class InternalError(pydantic.BaseModel):
    exception_info: ExceptionInfo = pydantic.Field(alias="exceptionInfo")

    class Partial(typing_extensions.TypedDict):
        exception_info: typing_extensions.NotRequired[ExceptionInfo]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @InternalError.Validators.root()
            def validate(values: InternalError.Partial) -> InternalError.Partial:
                ...

            @InternalError.Validators.field("exception_info")
            def validate_exception_info(exception_info: ExceptionInfo, values: InternalError.Partial) -> ExceptionInfo:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[InternalError.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[InternalError.Validators._RootValidator]] = []
        _exception_info_pre_validators: typing.ClassVar[
            typing.List[InternalError.Validators.PreExceptionInfoValidator]
        ] = []
        _exception_info_post_validators: typing.ClassVar[
            typing.List[InternalError.Validators.ExceptionInfoValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[InternalError.Validators._RootValidator], InternalError.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[InternalError.Validators._PreRootValidator], InternalError.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["exception_info"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [InternalError.Validators.PreExceptionInfoValidator], InternalError.Validators.PreExceptionInfoValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["exception_info"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [InternalError.Validators.ExceptionInfoValidator], InternalError.Validators.ExceptionInfoValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "exception_info":
                    if pre:
                        cls._exception_info_pre_validators.append(validator)
                    else:
                        cls._exception_info_post_validators.append(validator)
                return validator

            return decorator

        class PreExceptionInfoValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: InternalError.Partial) -> typing.Any:
                ...

        class ExceptionInfoValidator(typing_extensions.Protocol):
            def __call__(self, __v: ExceptionInfo, __values: InternalError.Partial) -> ExceptionInfo:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: InternalError.Partial) -> InternalError.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: InternalError.Partial) -> InternalError.Partial:
        for validator in InternalError.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: InternalError.Partial) -> InternalError.Partial:
        for validator in InternalError.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("exception_info", pre=True)
    def _pre_validate_exception_info(cls, v: ExceptionInfo, values: InternalError.Partial) -> ExceptionInfo:
        for validator in InternalError.Validators._exception_info_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception_info", pre=False)
    def _post_validate_exception_info(cls, v: ExceptionInfo, values: InternalError.Partial) -> ExceptionInfo:
        for validator in InternalError.Validators._exception_info_post_validators:
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
