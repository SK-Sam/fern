# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class FileInfoV2(pydantic.BaseModel):
    filename: str
    directory: str
    contents: str
    editable: bool

    class Partial(typing_extensions.TypedDict):
        filename: typing_extensions.NotRequired[str]
        directory: typing_extensions.NotRequired[str]
        contents: typing_extensions.NotRequired[str]
        editable: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FileInfoV2.Validators.root
            def validate(values: FileInfoV2.Partial) -> FileInfoV2.Partial:
                ...

            @FileInfoV2.Validators.field("filename")
            def validate_filename(v: str, values: FileInfoV2.Partial) -> str:
                ...

            @FileInfoV2.Validators.field("directory")
            def validate_directory(v: str, values: FileInfoV2.Partial) -> str:
                ...

            @FileInfoV2.Validators.field("contents")
            def validate_contents(v: str, values: FileInfoV2.Partial) -> str:
                ...

            @FileInfoV2.Validators.field("editable")
            def validate_editable(v: bool, values: FileInfoV2.Partial) -> bool:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[FileInfoV2.Partial], FileInfoV2.Partial]]] = []
        _filename_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.FilenameValidator]] = []
        _directory_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.DirectoryValidator]] = []
        _contents_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.ContentsValidator]] = []
        _editable_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.EditableValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[FileInfoV2.Partial], FileInfoV2.Partial]
        ) -> typing.Callable[[FileInfoV2.Partial], FileInfoV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"]
        ) -> typing.Callable[[FileInfoV2.Validators.FilenameValidator], FileInfoV2.Validators.FilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"]
        ) -> typing.Callable[[FileInfoV2.Validators.DirectoryValidator], FileInfoV2.Validators.DirectoryValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"]
        ) -> typing.Callable[[FileInfoV2.Validators.ContentsValidator], FileInfoV2.Validators.ContentsValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["editable"]
        ) -> typing.Callable[[FileInfoV2.Validators.EditableValidator], FileInfoV2.Validators.EditableValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    cls._filename_validators.append(validator)
                if field_name == "directory":
                    cls._directory_validators.append(validator)
                if field_name == "contents":
                    cls._contents_validators.append(validator)
                if field_name == "editable":
                    cls._editable_validators.append(validator)
                return validator

            return decorator

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: FileInfoV2.Partial) -> str:
                ...

        class DirectoryValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: FileInfoV2.Partial) -> str:
                ...

        class ContentsValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: FileInfoV2.Partial) -> str:
                ...

        class EditableValidator(typing_extensions.Protocol):
            def __call__(self, v: bool, *, values: FileInfoV2.Partial) -> bool:
                ...

    @pydantic.root_validator
    def _validate(cls, values: FileInfoV2.Partial) -> FileInfoV2.Partial:
        for validator in FileInfoV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("filename")
    def _validate_filename(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._filename_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("directory")
    def _validate_directory(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._directory_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("contents")
    def _validate_contents(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._contents_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("editable")
    def _validate_editable(cls, v: bool, values: FileInfoV2.Partial) -> bool:
        for validator in FileInfoV2.Validators._editable_validators:
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
