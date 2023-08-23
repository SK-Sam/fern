# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .error_info import ErrorInfo
from .graded_test_case_update import GradedTestCaseUpdate
from .recorded_test_case_update import RecordedTestCaseUpdate
from .running_submission_state import RunningSubmissionState


class TestSubmissionUpdateInfo_Running(pydantic.BaseModel):
    type: typing_extensions.Literal["running"]
    value: RunningSubmissionState


class TestSubmissionUpdateInfo_Stopped(pydantic.BaseModel):
    type: typing_extensions.Literal["stopped"]


class TestSubmissionUpdateInfo_Errored(pydantic.BaseModel):
    type: typing_extensions.Literal["errored"]
    value: ErrorInfo


class TestSubmissionUpdateInfo_GradedTestCase(GradedTestCaseUpdate):
    type: typing_extensions.Literal["gradedTestCase"]

    class Config:
        allow_population_by_field_name = True


class TestSubmissionUpdateInfo_RecordedTestCase(RecordedTestCaseUpdate):
    type: typing_extensions.Literal["recordedTestCase"]

    class Config:
        allow_population_by_field_name = True


class TestSubmissionUpdateInfo_Finished(pydantic.BaseModel):
    type: typing_extensions.Literal["finished"]


TestSubmissionUpdateInfo = typing.Union[
    TestSubmissionUpdateInfo_Running,
    TestSubmissionUpdateInfo_Stopped,
    TestSubmissionUpdateInfo_Errored,
    TestSubmissionUpdateInfo_GradedTestCase,
    TestSubmissionUpdateInfo_RecordedTestCase,
    TestSubmissionUpdateInfo_Finished,
]
