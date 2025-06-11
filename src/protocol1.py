from typing import Protocol


class NotifyImplementation(Protocol):
    def notify(self, to: str, subject: str, body: str) -> None:
        pass


class NotifyEmail:
    def notify(self, to: str, subject: str, body: str) -> None:
        print(f"Sending email to {to}: {subject} - {body}")


class NotificationManager:
    def __init__(self, notify_impl: NotifyImplementation) -> None:
        self.notify_impl = notify_impl

    def notify(self, user_email: str, message: str) -> None:
        self.notify_impl.notify(user_email, "Notification", message)


email_notifier = NotificationManager(NotifyEmail())
email_notifier.notify("user@example.com", "Hello from Dependency Injection")
