from typing import List
from django.core.mail import send_mail, send_mass_mail

from server import settings
from constants.email_constants import EmailConstants


def send_email(email_constants: EmailConstants) -> None:
    print(f"Sending Email to {email_constants.to}")

    send_mail(
        email_constants.subject,
        email_constants.body,
        settings.EMAIL_HOST_USER,
        [email_constants.to],
        fail_silently=False,
    )


def send_mass_email(email_constants: List[EmailConstants]) -> None:
    messages = []

    for email in email_constants:
        messages.append((email.subject, email.body, email.to))
        print(f"Sending mass emails to: {email.to}")

    send_mass_mail(messages, fail_silently=False)
