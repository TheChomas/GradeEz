from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.timezone import now as datetime_now
from constants.neural_constants import NeuralConstants

from utils import email_utils
from constants.email_constants import EmailConstants
from .models import Answer, Passage, Question, Quiz
from .forms import AnswerForm, QuizCustomForm
from .background import score_and_email

# Create your views here.


@login_required
def home(request, quiz_id):
    try:
        quiz = Quiz.objects.get(id=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("No Quizzes matches the given ID.")

    user = request.user
    print(f"Student ({user.username}) taking Quiz: ({quiz})")

    quizzes = user.quiz_set.all()

    if quiz in quizzes:
        raise Http404(
            "You seemed to have already taken this quiz. If this is a mistake please contact your faculty")

    if quiz.end_time < datetime_now():
        raise Http404(
            "Test time is over. You cannot access the quiz at this moment.")

    # try to keep multiple passages or change DB to make eaxh quiz hold
    # only one passage
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
        'questions': questions,
        'form': AnswerForm()
    }
    return render(request, "quiz/index.html", context)


@login_required
def submit_quiz(request, quiz_id):
    if request.method == "POST":
        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            raise Http404("No Quizzes matches the given ID.")

        try:
            passage = Passage.objects.get(quiz=quiz)
        except Passage.DoesNotExist:
            raise Http404("No Passages were in the given Quiz.")

        try:
            questions = Question.objects.filter(parent_passage=passage)
        except Question.DoesNotExist:
            raise Http404("No Questions were in the given Passage.")

        user = request.user
        print(f"Student: {user.username} submitting Quiz: {quiz_id}")

        data = dict(request.POST)
        data.pop("csrfmiddlewaretoken")

        question_answer_list = []
        answers = []

        for key, value in data.items():
            try:
                question = Question.objects.get(id=int(key))
            except Question.DoesNotExist:
                raise Http404("Error in processing data.")

            answers.append(value[0])

            answer = Answer(
                answer_text=value[0], parent_question=question, author=user)

            answer.save()

            # adding the students to the quiz list
            quiz.students.add(user)

            question_answer_list.append((question, answer))

        print(question_answer_list)

        score_and_email(username=user.username,
                        email=user.email,
                        quiz_id=quiz_id,
                        passage=passage.passage_text,
                        questions=[
                            question.question_text for question in questions],
                        answers=answers,
                        verbose_name=f"Emailing Score to user {user.email}",
                        schedule=datetime.now())

        print(f"Emailing scores to user {user.username}")

        # form = QuizCustomForm(request.POST, questions=questions)

        # print("Form not valid yet: ")
        # if form.is_valid():
        #     print("Form cleaned: ")
        #     print(form.cleaned_data)

        return render(request, "users/thankyou.html")
    else:
        return render(request, "users/404.html")


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
