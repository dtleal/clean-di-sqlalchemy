from dependency_injector import containers, providers
from frameworks.requests.manager import RequestsManager


class FrameworkContainer(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(
        modules=[
            "interface_adapters.api.v1.views.first_example",
        ],
    )
    config = providers.Configuration()

    requests_manager = providers.Factory(RequestsManager)
