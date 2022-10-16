from abc import ABC, abstractmethod
from typing import Any, Dict


class HttpRequester(ABC):
    """Http service interface"""

    @abstractmethod
    def get(self, url: str, params: Dict[str, Any] = None, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def post(
        self,
        url: str,
        headers: Dict[str, Any] = None,
        data: Dict[str, Any] = None,
        **kwargs: Any
    ) -> None:
        ...

    @abstractmethod
    def patch(self, url: str, data: Dict[str, Any] = None, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def put(self, url: str, data: Dict[str, Any] = None, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def delete(self, url: str, **kwargs: Any) -> None:
        ...
