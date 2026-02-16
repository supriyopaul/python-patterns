"""
Abstract Factory Pattern - Practice Problem 2 (Easy)
=====================================================

Furniture Shop (Simulation)
---------------------------

A furniture shop sells two styles of furniture: "Modern" and "Victorian".
For each style, they offer a Chair and a CoffeeTable.

We need a system where a client can furnish a room with items of a single style.

Requirements:
1.  Design a system that supports creating families of products (Chair, Table)
    for different styles (Modern, Victorian).
2.  The client code should request a "Chair" or "Table" from a factory, and
    receive the correct style automatically.
3.  Ensure that a Modern Chair is never mixed with a Victorian Table by mistake
    when using the factory.

Constraints & Tips:
- Focus on the "Family" aspect: The factory ensures products match.
- Use `print()` to simulate placing the furniture.

Example Output:
---------------
Placing Modern Chair
Placing Modern CoffeeTable
"""
