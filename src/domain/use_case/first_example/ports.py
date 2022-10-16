# pylint: disable=R0801,R0902
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class FirstExampleInputPort:
    """"""

    name: str
    active: Optional[bool]


@dataclass
class FirstExampleOutputPort():
    """Use case output port"""

    code: int
    body: Dict[str, Any]
