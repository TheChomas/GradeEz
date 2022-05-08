from typing import List
from background_task import background

from utils import email_utils, neural_utils
from constants.email_constants import EmailConstants
from constants import email_constants
from constants.neural_constants import NeuralConstants

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

    # parse and put scores in the email body

    print(f"Getting email ready...")
    email_obj = EmailConstants(
        subject=email_constants.EMAIL_SUBJECT + f" with ID {quiz_id}",
        body=email_constants.format_email_template(
            username=username,
            scores=scores,
            neural_obj=neural_obj),
        to=email)

    email_utils.send_email(email_obj)
