from domain.use_case.first_example.ports import FirstExampleInputPort, FirstExampleOutputPort
from interface_adapters.framework_services.interface.requests import HttpRequester


class FirstExampleUseCase():
    
    def __init__(self, http_requests: HttpRequester) -> None:
        self._http_requests = http_requests
    
    async def __call__(self, input_port: FirstExampleInputPort) -> FirstExampleOutputPort:
        self._http_requests.post(
            url="https://localhost:8080/items",
            headers=None,
            data={"item": "an awesome item", "price": 499}
        )
        return FirstExampleOutputPort(
            code=200, 
            body={
                "name": input_port.name,
                "active": input_port.active,
                "response": "May the force be with you!"
            }
        )
