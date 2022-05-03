from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

from utils import email_utils
from constants.email_constants import EmailConstants

# Create your views here.

to_address = "1nt18is076.kaushal@nmit.ac.in"
subject = "Testing"
body = "This is a test email from Django"


def home(request):
    print(f"Sending email to {to_address} about {subject}")
    email_utils.schedule_email(
        subject=subject, body=body, to=to_address,
        verbose_name=f"Email Score to user {to_address}",
        schedule=datetime.now())
    # email_utils.schedule_email(subject=subject, body=body, to=to_address, schedule=timedelta(minutes=1))

    return HttpResponse(f"Email sent to {to_address}")
