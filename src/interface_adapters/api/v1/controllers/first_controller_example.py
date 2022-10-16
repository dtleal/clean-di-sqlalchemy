from domain.use_case.first_example.first_example import FirstExampleUseCase
from interface_adapters.api.v1.dtos.first_example_dto import (
    FirstExampleInputDTO, FirstExampleOutputDTO
)
from domain.use_case.first_example.ports import FirstExampleInputPort


class FirstrExampleController():

    def __init__(
        self,
        first_example_use_case: FirstExampleUseCase,
    ) -> None:
        """"""
        self._first_example_use_case = first_example_use_case

    async def control(self, input_dto: FirstExampleInputDTO) -> FirstExampleOutputDTO:
        """"""
        input_port = FirstExampleInputPort(
            name = input_dto.name,
            active = input_dto.active,
        )
        use_case_output = await self._first_example_use_case(input_port=input_port)
        return FirstExampleOutputDTO(
            http_response_code=use_case_output.code,
            http_response_body=use_case_output.body
        )
