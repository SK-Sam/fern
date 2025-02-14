# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from .types.importing_type import ImportingType
from .types.optional_string import OptionalString

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FooClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find(
        self,
        *,
        optional_string: OptionalString,
        public_property: typing.Optional[str] = OMIT,
        private_property: typing.Optional[int] = OMIT
    ) -> ImportingType:
        """
        Parameters:
            - optional_string: OptionalString.

            - public_property: typing.Optional[str].

            - private_property: typing.Optional[int].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if public_property is not OMIT:
            _request["publicProperty"] = public_property
        if private_property is not OMIT:
            _request["privateProperty"] = private_property
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            self._client_wrapper.get_base_url(),
            params=remove_none_from_dict({"optionalString": optional_string}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ImportingType, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFooClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find(
        self,
        *,
        optional_string: OptionalString,
        public_property: typing.Optional[str] = OMIT,
        private_property: typing.Optional[int] = OMIT
    ) -> ImportingType:
        """
        Parameters:
            - optional_string: OptionalString.

            - public_property: typing.Optional[str].

            - private_property: typing.Optional[int].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if public_property is not OMIT:
            _request["publicProperty"] = public_property
        if private_property is not OMIT:
            _request["privateProperty"] = private_property
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            self._client_wrapper.get_base_url(),
            params=remove_none_from_dict({"optionalString": optional_string}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ImportingType, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
