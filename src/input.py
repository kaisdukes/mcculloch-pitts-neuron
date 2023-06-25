from dataclasses import dataclass

from .input_type import InputType


@dataclass
class Input:
    type: InputType
    value: bool
