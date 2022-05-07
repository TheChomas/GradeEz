from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.timezone import now as datetime_now

from utils import email_utils
from constants.email_constants import EmailConstants
from .models import Passage, Question, Quiz

# Create your views here.


@login_required
def home(request, quiz_id):
    print(f"Quiz id: {quiz_id}")

    try:
        quiz = Quiz.objects.get(id=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("No Quizzes matches the given ID.")

    if quiz.end_time < datetime_now():
        raise Http404(
            "Test time is over. You cannot access the quiz at this moment.")

    try:
        passage = Passage.objects.get(quiz=quiz)
    except Passage.DoesNotExist:
        raise Http404("No Passages were in the given Quiz.")

    try:
        questions = Question.objects.filter(parent_passage=passage)
    except Question.DoesNotExist:
        raise Http404("No Questions were in the given Passage.")

    context = {
        'end_date': quiz.end_time,
        'passage': passage,
        'quiz': quiz,
        'questions': questions
    }
    return render(request, "quiz/index.html", context)


def send_email(request):
    to_address = "1nt18is076.kaushal@nmit.ac.in"
    subject = "Testing"
    body = "This is a test email from Django"

    print(f"Sending email to {to_address} about {subject}")
    email_utils.schedule_email(
        subject=subject, body=body, to=to_address,
        verbose_name=f"Email Score to user {to_address}",
        schedule=datetime.now())
    # email_utils.schedule_email(subject=subject, body=body, to=to_address, schedule=timedelta(minutes=1))

    return HttpResponse(f"Email sent to {to_address}")
