"""
Factory Pattern - Practice Problem 5 (Expert)
==============================================

Cloud Resource Provisioner (Simulation)
---------------------------------------

Simulate provisioning resources (Storage, Compute) on different Clouds (AWS, Google).
We need a flexible system to create these resources without coupling the client
to specific provider classes.

Goal: Request a "storage" resource for "aws", and get an AWS-specific storage object.

Requirements:
1.  Design a system that can handle multiple providers (AWS, Google) and multiple
    resource types (Compute, Storage).
2.  The client should be able to specify the provider and resource type, and
    get the correct object back.
3.  The text output should clearly show which provider and resource was created.

Constraints & Tips:
- This touches on Abstract Factory but focuses on the creation logic.
- "Provisioning" just means creating the object and printing its status.

Example Output:
---------------
Provisioning AWS Compute...
AWS Compute Instance running.
"""
