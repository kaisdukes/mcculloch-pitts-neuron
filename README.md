# McCulloch-Pitts: The First Computational Neuron

[Dr. Kais Dukes](https://github.com/kaisdukes)

*This repository contains Python source code accompanying the article [McCulloch-Pitts: The First Computational Neuron](https://www.linkedin.com/pulse/mcculloch-pitts-first-computational-neuron-dr-kais-dukes). Published on LinkedIn on June 25, 2023.*

![](https://github.com/kaisdukes/mcculloch-pitts-neuron/blob/main/neuron.webp)

## Why am I writing this?

This year marks the 80th anniversary of the McCulloch-Pitts neuron. Because I’m passionate about the history of AI, I felt compelled to write about McCulloch-Pitts after reading a lot of misinformation online. New learners interested in the history of the field aren't being helped by an influx of low-quality, SEO-optimized articles appearing amongst the top Google results. There seems to be confusion around the specific contributions of the McCulloch-Pitts neuron (the threshold logic unit), and the Rosenblatt neuron (the perceptron). It’s also not clear whether McCulloch-Pitts is also a perceptron, and if it should be considered a weighted model.

To appeal to a wider audience, I've minimized technical jargon and provided simplified explanations. Despite being a mathematician at heart, I’ll also hold off from presenting math until towards the end of the article.

## What is the MCP Neuron in a Nutshell (Kurzgesagt-style)?

In a nutshell, the McCulloch-Pitts (MCP) model, one of the earliest and simplest models of neurons, was developed by Warren McCulloch and Walter Pitts in 1943, well over a decade before Rosenblatt’s work on perceptrons. The MCP neuron is a binary threshold neuron model, which means that the neuron either fires (outputs 1) or doesn’t fire (outputs 0) based on whether the sum of its inputs reaches a threshold or not. In reality, biological neurons are far more complex than MCP, but this model provided a crucial starting point for the mathematical modeling and understanding of neural networks and the development of modern AI.

## Wait, Wikipedia says that McCulloch-Pitts is a Perceptron!

The word ‘perceptron’ was coined by Rosenblatt in the 1950s while working at Cornell, building on the work of McCulloch and Pitts. However, like any word that gets overused, the term today has a broader meaning (semantic drift). In that sense you could call the original McCulloch-Pitts model a perceptron, but not in the stricter meaning of the term. This is confusing, so we should probably start at the beginning.

## McCulloch, Pitts and Turing

In 1943, McCulloch, a neurologist, and Pitts, a logician, published a curious and obscure article called: *A Logical Calculus of the Ideas Immanent in Nervous Activity*. Although their ideas took a while to gain traction and were almost completely ignored by the neuroscience community at the time, the article now has almost 30,000 citations.

What’s incredible about this paper is that it was the first computational theory of the brain. To give some historical context, McCulloch and Pitts were working within a community of neurologists and logicians who had only recently started to apply math to neurons. If you want more details on the history of this, I strongly recommend reading [Gualtiero Piccinni](https://en.wikipedia.org/wiki/Gualtiero_Piccinini)’s detailed review of the McCulloch-Pitts paper.

However, to give a brief background, the year they published their paper, 1943, is just a few years after 1936, when Alan Turing proposed the Turing Machine as a model of universal computation. It’s also a few years before 1950, when Turing proposed the Turing Test for Artificial Intelligence. It’s clear people at the time were thinking deeply about the links between logic, computation and the brain. One of McCulloch and Pitts' intentions was to create a simple model of neurons that could be used to build Turing machines.

## Biological Neurons

Mathematically, the McCulloch-Pitts neuron is simple. However, a network of MCP Neurons, which is capable of universal computation, is Turing complete.
Before getting into the math, let’s first talk a little bit about biological neurons. In basic terms, neurons are simply nerve cells in your body. They work using a combination of electricity and chemistry, and send electric signals to each other. They aren’t just in your brain, they're also in your eyes, your heart, your hands, and everywhere the brain needs to send and receive signals.

If you decide to pick something up, neurons in your brain send that signal all the way to the motor neurons in your hand through chains of neurons such as in your spine. This works both ways. If you place your hand over a fire, the sensory neurons in your hand will send a signal back to your brain, which will quickly decide to move your hand away.

Biological neurons, though complex and not yet fully understood, can be thought of at a high level in terms of axons, dendrites, and synapses A simplified view of this is that the axon is the nerve fiber cable that carries the electric signal out of a neuron. This is called the neuron 'firing’. Although almost all neurons have only one axon, the axon can branch out into thousands of nerve endings to make contact with other neurons.

Dendrites are the receiving side of this. A typical neuron would have one axon to send out its signal, and multiple dendrites to receive inputs. Synapses are where the axon of one neuron interfaces with the dendrite of another neuron. Axons and dendrites don’t actually touch. Chemicals called neurotransmitters send signals across the synapse. Communication goes from electrical, to chemical, and then back to electrical.

## The Neuroscience behind the McCulloch-Pitts Neuron

In their groundbreaking 1943 paper, McCulloch and Pitts start with 4 facts from the neuroscience known at the time:

1. The brain is composed of neurons
2. Neurons connect through synapses
3. Neurons can send either excitatory or inhibitory signals to each other
4. A neuron only fires when it reaches a certain threshold of excitatory input signals

Amazingly, these facts still hold true today at a fundamental level, although our understanding of the brain and its processes have expanded vastly since then. For example, we now know much more about the wide variety of neurotransmitters and the essential role of both neurons and glial cells in the brain. However, the beauty of the McCulloch-Pitts model lies in its simplicity, which served as a key step towards the development of full artificial neural networks.

## The McCulloch-Pitts Neuron and Rosenblatt’s Perceptron 

There are several key differences between the MCP neuron and the later Rosenblatt perceptron.

**Unweighted:** The MCP neuron is generally considered to be an unweighted model. In its simplest form, there are no weights between neurons, meaning all input signals are considered to have the same strength. In contrast, Rosenblatt's perceptron model introduces weights to modulate the effect of each input, reflecting the fact that different inputs may have different levels of importance.

**Binary:** The MCP neuron model is a binary threshold model that, given its foundations in logic, works with only Boolean values (true or false) or binary (1 or 0). This is in contrast to the continuous real numbers used in Rosenblatt’s perceptron. The inputs and output are binary, and the neuron fires or doesn't fire based on whether the sum of inputs reaches a certain threshold.

**Inhibitory:** Inhibitory signals act as a veto; if any inhibitory input signal is present, the neuron won’t fire, regardless of the contributions from the excitatory inputs. The negative weights in Rosenblatt’s perceptron also serve an inhibitory role, as they reduce the weighted sum and hence the likelihood of the perceptron firing. But this is not the same as the inhibitory mechanism in the MCP model, which is explicit.

**Fixed design:** The original MCP neuron model didn't provide a learning algorithm, meaning that once the network architecture was set, it remained fixed. It was McCulloch and Pitts' intention to create a simplified theoretical model of a neuron that could be used to design Turing machines, rather than a system that could learn. Rosenblatt’s perceptron, however, crucially introduced a learning algorithm that adjusted weights based on errors made by the model. This is why perceptrons are key to understanding the history of modern machine learning and AI.

## Universal Computation

Time for some basic math! Let’s now see how a network of MCP neurons (McCulloch-Pitts nets) can indeed support universal computation and are Turing complete. The key to this is the inhibitory signals. It is well known that a universal computer can be built just out of NAND gates (for details see this excellent Wikipedia article on [NAND logic](https://en.wikipedia.org/wiki/NAND_logic)). Therefore, we need to demonstrate that we can build NOT and AND gates using MCP neurons.

**NOT gate:** To build a NOT gate, we take a single MCP neuron with threshold zero, connected to a single inhibitory input. When the inhibitory input is on (1), the neuron won't fire (0). When the inhibitory input is off (0), the total input signal is zero, which means we've reached our threshold and the neuron fires (1).

**AND gate:** To build an AND gate, we connect to two excitatory inputs to an MCP neuron with threshold 2. Both inputs have to be on (1) for the threshold to trigger the neuron firing (1). If either input or both are 0, the neuron won't fire as the summed input won't reach the threshold. This matches the AND gate’s truth table.

## The Minsky Controversy

For those interested in more of a historical deep dive, in 1969 Minsky and Papert published a book on perceptrons. This was the same year that Minsky also received the prestigious Turing Award for his contributions to AI. Minsky is widely considered to be one of the founding pioneers of Artificial Intelligence.

His book, along with other factors such as a bad economy and researchers overpromising on AI, contributed to the onset of the 'AI winter' that lasted until the 1990s. Funding for neural AI research was cut dramatically, setting the field back by decades.

This is a somewhat controversial subject in the AI community. Some claim the AI winter was worsened by Minsky highlighting that a single perceptron is unable to compute the XOR function, as it’s not linearly separable. This may have led to neural networks not being considered a promising line of scientific investigation.

Despite today's advances in AI and neural networks making this seem unbelievable, Minsky's influence led to a redirection of funding away from neural methods, causing significant disruption in research.

It's astonishing that Minsky's critique focused solely on the limitations of a single neuron. Minsky and Papert were not ignorant of the potential of multilayer networks; their book actually includes a chapter acknowledging that multilayer perceptrons could in theory overcome the limitations they highlighted. However, they argued that there was no known efficient way to train such networks, a problem that was not resolved until the rediscovery of backpropagation in the mid-1980s.

Although there doesn’t appear to be a historical consensus on why this misunderstanding occurred, it was definitely known to some in the AI community at the time that networks of neurons could approximate arbitrary functions. Rosenblatt published results to this effect in 1961. However, soon after Minsky's book was published, he sadly died in a sailing accident on his 43rd birthday in 1971.

These historical circumstances, driven by unfortunate events and misunderstandings, profoundly influenced the pace and direction of AI development. However, as we continue to stand on the shoulders of giants like McCulloch, Pitts, Rosenblatt, and Turing, it's incredibly exciting to imagine the breakthroughs the next 80 years will bring.

# Getting Started

This project uses [Poetry](https://python-poetry.org).

First, clone the repository:

```
git clone https://github.com/kaisdukes/mcculloch-pitts-neuron.git
cd mcculloch-pitts-neuron
```

Install Poetry using [Homebrew](https://brew.sh):

```
brew install poetry
```

Use the Poetry shell:

```
poetry shell
```

Test the neuron:

```
python tests/neuron_test.py
```