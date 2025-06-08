from collections.abc import Callable


def send_email(to: str, subject: str, body: str) -> None:
    print(f"Sending email to {to}: {subject} - {body}")


class NotificationManager:
    def __init__(self, notify_impl: Callable[[str], str]) -> None:
        self.notify_impl = notify_impl

    def notify(self, user_email: str, message: str) -> None:
        self.notify_impl(user_email, "Notification", message)


email_notifier = NotificationManager(send_email)
email_notifier.notify("user@example.com", "Hello from Dependency Injection")
