# Vexecuteable
> A visual programming language that can compile to any language.

> ⚠️ **PROJECT STATUS: Currently in development. NOT USABLE YET.**


**Table of Contents**
- [What is Vexecuteable?](#what-is-vexecuteable)
- [What it is and what it is not](#what-it-is-and-what-it-is-not)
  - [What it is](#what-it-is)
  - [What it is not](#what-it-is-not)
- [How it works](#how-it-works)
  - [The internal representation](#the-internal-representation)
  - [The compiler](#the-compiler)
  - [The interpreter](#the-interpreter)
  - [The visual editor/node graph](#the-visual-editornode-graph)
- [Future plans](#future-plans)


# What is Vexecuteable?

Vexecuteable is a visual programming language that can compile to any language*.

It is inspired by [Blueprints](https://docs.unrealengine.com/en-US/Engine/Blueprints/index.html) from [Unreal Engine](https://www.unrealengine.com/en-US/what-is-unreal-engine-4) of [Epic Games](https://www.epicgames.com/).

It uses a [graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) to represent the program.

# What it is and what it is not

## What it is

- A visual programming language
- A compiler
- A graph editor/visualizer
- An interpreter
- A transpiler

## What it is not

- A code generator
- A visual scripting language
- A flowchart (although it can be used to create flowcharts)
- A flowchart to code converter/generator

# How it works

## The internal representation
It uses protobuf to represent the graph. ([why protobuf?](https://developers.google.com/protocol-buffers/docs/overview))

## The compiler
Not implemented yet.

## The interpreter
It uses [Python](https://www.python.org/) to interpret the graph.

## The visual editor/node graph
It uses [Dear ImGui](https://github.com/ocornut/imgui) to render the graph.

## Future plans
- [ ] Migrate to C++ (from Python)
- - [ ] Implement the compiler
- - [ ] Implement the interpreter
- - [ ] Implement the visual editor
- - [ ] Implement the protobuf parser
- [ ] Make the compiler transpile to Python
