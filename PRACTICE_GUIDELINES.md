# Practice Problem Guidelines and Template

## Core Philosophy
1.  **Doable in 15 Minutes**: Each problem must be solvable within 10-15 minutes of focused coding.
2.  **Pure Python**: No external dependencies (databases, cloud SDKs, APIs) required.
    *   **Simulation Only**: Any external system should be simulated with prints or in-memory data structures.
3.  **Self-Contained**: The problem description should provide all necessary context without needing to hunt for docs.
4.  **Testable**: The solution must be verifiable with simple `assert` statements or clear print outputs.
5.  **Pattern Focused**: The problem must force the use of the specific pattern to solve a design issue, not just "write a class".

## Template for Problem Files

Each practice file should follow this structure in its docstring:

```python
"""
[Pattern Name] - Practice Problem [Number] ([Difficulty])
==========================================================

[Scenario Title]
----------------

[Scenario Description]
Explain the real-world scenario. Keep it relatable but simplified.
e.g., "A logistics company needs to route packages..." instead of "Class A needs to call Class B".

[The Design Issue]
Explain why a simple approach fails or is rigid.
e.g., "Currently, adding a new transport type requires changing the main routing logic."

Requirements:
1.  [Required Class/Interface 1] - Explain its role (e.g., "Transport interface with deliver method").
2.  [Required Class/Interface 2] - Explain its role.
3.  [The Pattern Component] - e.g., "A Factory class that takes a type string and returns the Transport."
4.  [Execution] - "Demonstrate creating different transports using the factory."

Constraints & Tips:
- Do not use external libraries.
- Use print statements to simulate actions (e.g., print("Truck delivering...")).
- Focus on the structure of the classes.

Example Output:
---------------
Truck delivering package #123
Ship delivering package #456
"""

## Difficulty Levels

| Level | Description |
| :--- | :--- |
| **Beginner** | Basic implementation of the pattern structure. No complex logic. |
| **Easy** | Pattern with 1-2 variations or parameters. |
| **Intermediate** | Pattern with meaningful configuration or state. |
| **Advanced** | Combining the pattern with another concept (e.g., Registry, dynamic loading). |
| **Expert** | Real-world simulation, handling edge cases, or "meta" implementations. |
