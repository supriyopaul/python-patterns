# Self-Evaluation Guide for Design Patterns

Use this guide to self-assess your practice solutions. A robust implementation of any design pattern should meet these general quality criteria.

## General Design Quality

- [ ] **Client Decoupling**: Does the client code work primarily with interfaces/abstractions rather than concrete classes?
- [ ] **Open/Closed Principle**: Can you add a new variation (e.g., a new product type) without modifying existing client logic?
- [ ] **Single Responsibility**: Does each class have one clear job? (e.g., a Factory creates, a Product performs the action).
- [ ] **No Leaky Abstractions**: Do all concrete implementations share the exact same method signatures? The client should not need to pass different arguments based on the specific type it received.

## Implementation Checklist

- [ ] **Unified Interface**: Use Protocols or Abstract Base Classes to enforce a common interface for all interchangeable parts.
- [ ] **Encapsulated Complexity**: Complex logic (like `if/else` chains for creation) should be hidden within a Factory or Builder, not exposed in the `main` execution block.
- [ ] **Type Safety**: Are return types hinted as the abstract interface rather than a specific concrete class?
- [ ] **Testability**: Can you verify the behavior with simple assertions or print statements without needing extensive setup?

## Common Red Flags

1.  **Type Checking in Client**: If you see `if isinstance(obj, ConcreteType):` in your usage code, the abstraction has failed.
2.  **Inconsistent Methods**: If one class has `send(msg)` and another has `send(msg, recipient)`, they are not interchangeable.
3.  **Hardcoded Dependencies**: The client code should not directly instantiate concrete helper classes if the pattern is meant to abstract them.
