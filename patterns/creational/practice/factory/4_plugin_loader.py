"""
Factory Pattern - Practice Problem 4 (Advanced)
================================================

Plugin Loader (Simulation)
--------------------------

We want a system that can "load" plugins by name.
Instead of loading files, we will register classes in a dictionary.

Requirements:
1.  Design a plugin system where new plugin types can be registered dynamically
    at runtime (e.g., associating a name like "video" with a VideoPlugin class).
2.  The factory should be able to instantiate a plugin given its registered name.
3.  Demonstrate registering a custom plugin and then creating an instance of it
    via the factory.

Constraints & Tips:
- Think about how to store the mapping between names and classes.
- This is a "Registration Factory" variation.

Example Output:
---------------
Video Plugin playing 4k video...
Audio Plugin playing surround sound...
"""
