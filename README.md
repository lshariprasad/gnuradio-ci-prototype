# GNU Radio CI Prototype

This project demonstrates automated testing of GNU Radio flowgraphs using Python.

## Features
- Runs a simple flowgraph
- Captures output samples
- Logs execution

## Goal
Foundation for Hardware-in-the-Loop CI system for GNU Radio.

## Automated Testing Output

Each CI run generates structured results:

```json
{
  "samples": 5,
  "status": "PASS"
}