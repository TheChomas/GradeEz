from typing import List
from background_task import background
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from constants.email_template_constants import EmailTemplate
from django.contrib.auth.models import User

from utils import email_utils, neural_utils
from constants.email_constants import EmailConstants
from constants import email_constants
from constants.neural_constants import NeuralConstants
from quiz.models import Answer

model = neural_utils.start_model()


@background(schedule=1)
def score_and_email(quiz_id: int, username: str, email: str, passage: str, questions: List[str], answers: List[str]):
    # if model is None:
    #     print("Getting the model ready...")
    #     model = neural_utils.start_model()
    # else:
    #     print("Model is already loaded. Proceeding...")

    print(f"Getting scores from AI model")
    neural_obj = NeuralConstants(passage, questions, answers)

    scores = neural_utils.get_score(
        model, neural_obj.passage, neural_obj.questions, neural_obj.answers)

    user = User.objects.get(username=username)

    # save the scores to the DB
    for score, answer in zip(scores, answers):
        a = Answer.objects.get(answer_text=answer, author=user)
        a.score = 1 if score > 0.4 else 0
        a.save()

    # parse and put scores in the email body

    print(f"Getting email ready...")

    final_score = sum(
        [1 if score > 0.4 else 0 for score in scores])

    questions_to_send = []

    for question, answer, score in zip(questions, answers, scores):
        questions_to_send.append(EmailTemplate(
            question, answer, round(score, 2)))

    context = {
        'username': username,
        'final_score': final_score,
        'questions': questions_to_send
    }

    html_message = render_to_string('quiz/email.html', context)
    plain_message = strip_tags(html_message)

    email_obj = EmailConstants(
        subject=email_constants.EMAIL_SUBJECT + f" with ID {quiz_id}",
        # body=email_constants.format_email_template(
        #     username=username,
        #     scores=scores,
        #     neural_obj=neural_obj),
        body=plain_message,
        to=email)

    email_utils.send_email_html(email_obj, html_message)
