import logging
import sys
from fastapi import FastAPI
from interface_adapters.api.v1.views import first_example
from fastapi import APIRouter


logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s %(filename)s %(funcName)s: %(message)s',
    level=logging.INFO
)


class FastApiManager():
    
    def __init__(self, app: FastAPI) -> None:
        self._app = app
        self._logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    def initialize_cors(self) -> None:
        pass
    
    def initialize_limiter(self) -> None:
        pass

    def initialize_routers(self) -> None:
        self._logger.info("Adding routes...")
        api_router = APIRouter()
        api_router.include_router(first_example.router, prefix="/v1", tags=["Example"])
        self._app.include_router(api_router)

    def get_instance(self) -> FastAPI:
        return self._app
