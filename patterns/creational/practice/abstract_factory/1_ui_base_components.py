"""
Abstract Factory Pattern - Practice Problem 1 (Beginner)
=========================================================

UI Base Components (Simulation)
-------------------------------

We need to create a UI toolkit that supports two themes: "Light" and "Dark".
Each theme has its own version of a Button and a Checkbox.

The client code should be able to create a Button or Checkbox without knowing
which theme is currently active.

Requirements:
1.  Define abstract product interfaces: `Button` and `Checkbox`.
    - Both should have a `paint()` method.
2.  Create concrete products:
    - `LightButton`, `DarkButton`
    - `LightCheckbox`, `DarkCheckbox`
3.  Define the Abstract Factory interface `GUIFactory` with methods:
    - `create_button()`
    - `create_checkbox()`
4.  Create concrete factories `LightFactory` and `DarkFactory`.
5.  Demonstrate creating a factory (e.g., LightFactory) and using it to
    create a button and checkbox, then painting them.

Constraints & Tips:
- Use simple `print` statements in `paint()` (e.g., "Rendering Light Button").
- The client code should only interact with the abstract interfaces.

Example Output:
---------------
Rendering Light Button
Rendering Light Checkbox
"""
