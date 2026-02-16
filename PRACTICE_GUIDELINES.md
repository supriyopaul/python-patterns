# Practice Problem Guidelines and Template

## Core Philosophy
1.  **Doable in 15 Minutes**: Each problem must be solvable within 10-15 minutes of focused coding.
2.  **Pure Python**: No external dependencies (databases, cloud SDKs, APIs) required.
    *   **Simulation Only**: Any external system should be simulated with prints or in-memory data structures.
3.  **Self-Contained**: The problem description should provide all necessary context without needing to hunt for docs.
4.  **Testable**: The solution must be verifiable with simple `assert` statements or clear print outputs.
5.  **Pattern Focused**: The problem must force the use of the specific pattern to solve a design issue.
6.  **Progressive Difficulty & Hints**:
    *   **Beginner**: Explicit structural hints (e.g., "Create a class X").
    *   **Intermediate+**: Functional requirements only (e.g., "The system must support..."). No implementation hand-holding.

## Template for Problem Files

Each practice file should follow this structure in its docstring:

```python
"""
[Pattern Name] - Practice Problem [Number] ([Difficulty])
==========================================================

[Scenario Title]
----------------

[Scenario Description]
Explain the real-world scenario.

[The Design Issue]
Explain the problem (e.g. tight coupling, complex creation logic).

Requirements:
1.  [Functional Requirement 1] - e.g. "We need to support X, Y, and Z types."
2.  [Functional Requirement 2] - e.g. "Client code should not know concrete classes."
3.  [Execution] - "Demonstrate the solution."

Constraints & Tips:
- Do not use external libraries.
- Use print statements to simulate actions.

Example Output:
---------------
[Expected Output]
"""

## Difficulty Levels

| Level | Description | Hint Level |
| :--- | :--- | :--- |
| **Beginner** | Basic implementation. | **High** (Class structure provided) |
| **Easy** | Pattern with variations. | **Medium** (Key components suggested) |
| **Intermediate** | Configuration/State. | **Low** (Functional goals only) |
| **Advanced** | Combined patterns. | **None** (Problem statement only) |
| **Expert** | Real-world simulation. | **None** (Complex scenario) |
