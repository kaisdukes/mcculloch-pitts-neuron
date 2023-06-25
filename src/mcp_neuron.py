from dataclasses import dataclass
from typing import List

from .input import Input
from .input_type import InputType


@dataclass
class McpNeuron:
    inputs: List[Input]
    threshold: int

    def fire(self):
        sum_excitatory = sum(input.value for input in self.inputs if input.type == InputType.EXCITATORY)
        has_inhibitory = any(input.value for input in self.inputs if input.type == InputType.INHIBITORY)

        return sum_excitatory >= self.threshold and not has_inhibitory
