# Self-Evaluation Guide for Practice Problems

Use this guide to check your solutions. A good implementation should meet these criteria.

## General Principles

- [ ] **No `if/else` checks for types in client code**: The client should not need to check `if type == "A"` to use the object.
- [ ] **Unified Interface**: All products (e.g., `EmailNotifier`, `SMSNotifier`) must have the exact same method signatures.
- [ ] **Duck Typing / Protocols**: The classes don't need to inherit from a base class, but they must satisfy the shared Protocol.
- [ ] **Factory Encapsulation**: The complex creation logic (e.g., deciding which class to instantiate) should be hidden inside the Factory.

## Specific Pattern Checklists

### Factory Pattern
- [ ] **Does the Factory return a generic interface?** The return type hint should be the Protocol (e.g., `-> Notifier`), not a concrete class.
- [ ] **Is the Client isolated?** The code calling the factory should not import the concrete classes (`EmailNotifier`, `SMSNotifier`).
- [ ] **Can you add a new type?** Adding a new type (e.g., `SlackNotifier`) should only require changing the Factory, not the Client code.

### Abstract Factory
- [ ] **Are there families of products?** (e.g., `WindowsButton` + `WindowsCheckbox` vs `MacButton` + `MacCheckbox`).
- [ ] **Does the client use the factory abstractly?** `factory.create_button()` should return the right button for the current OS/theme without the client asking for it specifically.

### Builder Pattern
- [ ] **Is construction separated from representation?** Can you reuse the same construction steps to build different object representations?
- [ ] **Does it handle complex objects?** Use this when a constructor would have too many parameters (telescoping constructor problem).

### Singleton (Borg/Module)
- [ ] **Is state shared?** If you create two instances, do they share the same data?
- [ ] **Is it thread-safe?** (If applicable).

## Common Mistakes to Avoid

1.  **Leaky Abstractions**: If `EmailNotifier.send()` takes `subject` but `SMSNotifier.send()` takes `number`, your interface is broken.
2.  **Factory doing too much**: The factory should create objects, not run their business logic.
3.  **Client instantiation**: If you see `MyClass()` in the client code (outside the factory), you bypassed the pattern.
