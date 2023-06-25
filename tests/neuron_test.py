import unittest

from src.input import Input
from src.input_type import InputType
from src.logic_gates import and_gate, not_gate
from src.mcp_neuron import McpNeuron


class NeuronTest(unittest.TestCase):

    def test_mcp_neuron(self):
        neuron = McpNeuron(
            inputs=[
                Input(type=InputType.EXCITATORY, value=True),
                Input(type=InputType.INHIBITORY, value=False)],
            threshold=1)
        self.assertEqual(neuron.fire(), True)

        neuron = McpNeuron(
            inputs=[
                Input(type=InputType.EXCITATORY, value=True),
                Input(type=InputType.INHIBITORY, value=True)],
            threshold=1)
        self.assertEqual(neuron.fire(), False)

    def test_not_gate(self):
        self.assertEqual(not_gate(True), False)
        self.assertEqual(not_gate(False), True)

    def test_and_gate(self):
        self.assertEqual(and_gate(True, True), True)
        self.assertEqual(and_gate(True, False), False)
        self.assertEqual(and_gate(False, True), False)
        self.assertEqual(and_gate(False, False), False)


if __name__ == '__main__':
    unittest.main()
