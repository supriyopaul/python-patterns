"""
Factory Pattern - Practice Problem 2 (Easy)
============================================

Notification Service (Simulation)
---------------------------------

An application sends notifications via Email, SMS, or Push.
We want to simulate sending these messages without real APIs.

The system receives the preferred channel and a message, then "sends" it.

Requirements:
1.  Define a `Notifier` interface with a `send(message)` method.
2.  Create `EmailNotifier`, `SMSNotifier`, and `PushNotifier`.
    - `send(message)` should print: "Sending Email: [message]", etc.
3.  Create a `NotificationFactory` that takes a channel name (e.g., "email")
    and returns the correct notifier.
4.  Demonstrate usage: Get a notifier for "sms" and send "Hello World".

Constraints & Tips:
- No real APIs needed. Just use `print()`.
- Handle invalid channel names gracefully (e.g., raise ValueError).

Example Output:
---------------
Sending SMS: Hello World
Sending Email: Welcome aboard!
"""
