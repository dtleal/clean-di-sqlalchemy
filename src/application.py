from fastapi import FastAPI
from frameworks.fast_api.manager import FastApiManager
from frameworks.container import FrameworkContainer


def initialize() -> FastAPI:
    try:
        app = FastApiManager(app=FastAPI())
        app.initialize_cors()
        app.initialize_limiter()
        app.initialize_routers()
        __initialize_framework_container()
        return app.get_instance()

    except Exception as error:
        raise("An excepetion has ocurred trying to initialize FastApi: ", error)

def __initialize_framework_container() -> None:
        container = FrameworkContainer()
        container.wire(modules=[__name__])
