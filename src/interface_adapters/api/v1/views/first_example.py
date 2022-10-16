from fastapi import APIRouter,Depends
from dependency_injector.wiring import Provide, inject

from interface_adapters.api.v1.controllers.first_controller_example import FirstrExampleController
from interface_adapters.api.v1.dtos.first_example_dto import (
    FirstExampleInputDTO, FirstExampleOutputDTO
)
from domain.use_case.first_example.first_example import FirstExampleUseCase
from interface_adapters.framework_services.interface.requests import HttpRequester
from frameworks.container import FrameworkContainer

router = APIRouter()


@router.post(
    "/first-example",
    response_model=FirstExampleOutputDTO
)
@inject
async def first_example_route(
    input_dto: FirstExampleInputDTO,
    requests_manager: HttpRequester = Depends(Provide[FrameworkContainer.requests_manager])
) -> FirstExampleOutputDTO:
    """"""
    first_example_use_case = FirstExampleUseCase(http_requests=requests_manager)
    controller = FirstrExampleController(first_example_use_case=first_example_use_case)
    return await controller.control(input_dto)
