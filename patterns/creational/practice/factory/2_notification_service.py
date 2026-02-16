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

from typing import Protocol

class Notifier(Protocol):
    def send(self, message, to):
        pass

class EmailNotifier:
    def send(self, message, to):
        return "Sent an email notification to: {to}\n with body:{message}".format(to=to, message=message)

class SMSNotifier:
    def send(self, message, to):
        return "Sent an SMS notification to: {to}\n message: {message}".format(to=to, message=message)

def send_notification(notificationtype="Email") -> Notifier:
    if notificationtype == "Email":
        return EmailNotifier()
    elif notificationtype == "SMS":
        return SMSNotifier()
    else:
        raise ValueError("Wrong notification type")

if __name__ == "__main__":
    print(send_notification("SMS").send(message="Sample message", to=123456789))
    print(send_notification("Email").send(message="body of the email", to="paul.supriyo@gmail.com"))
    print(send_notification("Email").send(message="body of the email")) #wrong
    print(send_notification("Slack").send())
