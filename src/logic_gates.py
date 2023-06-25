from .input import Input
from .input_type import InputType
from .mcp_neuron import McpNeuron


def not_gate(a: bool):
    neuron = McpNeuron(
        inputs=[Input(type=InputType.INHIBITORY, value=a)],
        threshold=0)

    return neuron.fire()


def and_gate(a: bool, b: bool):
    neuron = McpNeuron(
        inputs=[
            Input(type=InputType.EXCITATORY, value=a),
            Input(type=InputType.EXCITATORY, value=b)],
        threshold=2)

    return neuron.fire()
