"""
Factory Pattern - Practice Problem 4 (Advanced)
================================================

Plugin Loader (Simulation)
--------------------------

We want a system that can "load" plugins by name.
Instead of loading files, we will register classes in a dictionary.

Requirements:
1.  Define a `Plugin` interface with a `perform_action()` method.
2.  Create `AudioPlugin` and `VideoPlugin`.
    - `perform_action()` prints something specific.
3.  Create a `PluginFactory` that allows registering new plugins.
    - method `register(name, plugin_class)`
    - method `get_plugin(name)` -> returns a new instance of that class.
4.  Register your plugins manually, then ask the factory for "video"
    and call `perform_action()`.

Constraints & Tips:
- Use a dictionary in the factory to map names to classes.
- e.g., `_registry = {}`
- This is a "Registration Factory" variation.

Example Output:
---------------
Video Plugin playing 4k video...
Audio Plugin playing surround sound...
"""
