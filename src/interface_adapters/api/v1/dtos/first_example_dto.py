from pydantic import BaseModel
from pydantic import Field
from typing import Optional, Any, Dict


class FirstExampleInputDTO(BaseModel):

    name: str = Field(default=None)
    active: Optional[bool] = Field(default=False)


class FirstExampleOutputDTO(BaseModel):

    http_response_code: int
    http_response_body: Dict[str, Any]
