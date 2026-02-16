"""
Factory Pattern - Practice Problem 2 (Easy)
============================================

Notification Service (Simulation)
---------------------------------

An application sends notifications via Email, SMS, or Push.
We want to simulate sending these messages without real APIs.

The system receives the preferred channel and a message, then "sends" it.

Requirements:
1.  Design a system where the client code can request a notifier for a specific
    channel (e.g., "email", "sms") without knowing the concrete class.
2.  Each notifier should handle the "sending" action (simulated with print).
3.  Demonstrate usage: Get a notifier for "sms" and send "Hello World".

Constraints & Tips:
- No real APIs needed. Just use `print()`.
- Handle invalid channel names gracefully.

Example Output:
---------------
Sending SMS: Hello World
Sending Email: Welcome aboard!
"""
