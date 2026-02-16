"""
Factory Pattern - Practice Problem 5 (Expert)
==============================================

Cloud Resource Provisioner (Simulation)
---------------------------------------

Simulate provisioning resources (Storage, Compute) on different Clouds (AWS, Google).
We need a "Factory of Factories" (Abstract Factory hint, but doable with simple Factory logic).

Goal: Request a "storage" resource for "aws", and get an "AWSStorage" object.

Requirements:
1.  Define simple classes: `AWSStorage`, `GoogleStorage`, `AWSCompute`, `GoogleCompute`.
    - Each has a `status()` method returning e.g., "AWS Storage Bucket Online".
2.  Create a `CloudFactory` with a static method `get_factory(provider)`.
    - Returns an `AWSFactory` or `GoogleFactory`.
3.  `AWSFactory` has `create_resource(type)` returning AWS objects.
4.  `GoogleFactory` has `create_resource(type)` returning Google objects.
5.  Client Code:
    - Get AWS factory.
    - Create "compute".
    - Print status.

Constraints & Tips:
- This touches on Abstract Factory but focuses on the creation logic.
- Keep classes empty except for the `status()` print method.
- "Provisioning" just means creating the object.

Example Output:
---------------
Provisioning AWS Compute...
AWS Compute Instance running.
"""
