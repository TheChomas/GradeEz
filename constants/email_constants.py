

from math import ceil
from typing import List

from constants.neural_constants import NeuralConstants


EMAIL_SUBJECT = "Scores computed at your recent test at GradeEz"


def format_email_template(username: str, scores: List[float], neural_obj: NeuralConstants) -> None:
    final_score = sum(
        [1 if score > 0.4 else 0 for score in scores])

    question_wise_result = ""

    for question, answer, score in zip(neural_obj.questions, neural_obj.answers, scores):
        res = f"Question: {question}\n"
        res += f"Your answer: {answer}\n"
        res += "Score: %.2f" % score + "\n"
        res += "---------\n"

        question_wise_result += res

    return f"""
Hey {username}, our AI model has finished correcting your test, and it has given the below scores:

Your final score is {round(final_score, 1)} out of {len(scores)}.

Question wise score:
{question_wise_result}


If you have any queries or think our AI has not corrected fairly, 
you can get in contact with the faculty who sent you the quiz link.

Regards,
The GradeEz team.
"""

#     return f"""
# <h2>Hey {username}, our AI model has finished correcting your test, and it has given the below scores:</h2>

# <h3>Your final score is {round(final_score, 1)} out of {len(scores)}.</h3>

# <h3>Question wise score:</h3>
# {question_wise_result}


# If you have any queries or think our AI has not corrected fairly,
# you can get in contact with the faculty who sent you the quiz link.

# <h5>Regards,</h5>
# <h6>The GradeEz team.</h6>
# """


class EmailConstants:
    subject = ""
    body = ""
    to = ""

    def __init__(self, subject: str, body: str, to: str) -> None:
        self.subject = subject
        self.body = body
        self.to = to

    def get_dict(self) -> dict:
        return {
            "subject": self.subject,
            "body": self.body,
            "to": self.to
        }
