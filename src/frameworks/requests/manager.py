import json
import logging
from dataclasses import dataclass
from typing import Any, Dict

import requests
from interface_adapters.framework_services.interface.requests import HttpRequester


@dataclass
class RequestsResponse():
    """Http response handler"""

    code: int
    body: Dict[str, Any]

    @classmethod
    def build_from_request_response(cls, response: requests.Response) -> requests.Response:
        return cls(code=response.status_code, body=response.json())


class RequestsManager(HttpRequester):
    """Http request manager"""

    def __init__(self) -> None:
        self._logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    def get(
        self, url: str, params: Dict[str, Any] = None, **kwargs: Any
    ) -> RequestsResponse:
        """Http get method"""

    def post(
        self,
        url: str,
        headers: Dict[str, Any] = None,
        data: Dict[str, Any] = None,
        **kwargs: Any,
    ) -> RequestsResponse:
        """Http post method"""
        response = requests.post(url=url, headers=headers, data=json.dumps(data))
        return RequestsResponse.build_from_request_response(response=response)

    def patch(
        self, url: str, data: Dict[str, Any] = None, **kwargs: Any
    ) -> RequestsResponse:
        """Http patch method"""

    def put(
        self, url: str, data: Dict[str, Any] = None, **kwargs: Any
    ) -> RequestsResponse:
        """Http put method"""

    def delete(self, url: str, **kwargs: Any) -> RequestsResponse:
        """Http delete method"""
