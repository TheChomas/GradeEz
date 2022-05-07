
from typing import List


class NeuralConstants:
    passage = ""
    questions = []
    answers = []

    def __init__(self, passage: str, questions: List[str], answers: List[str]) -> None:
        self.passage = passage
        self.questions = questions.copy()
        self.answers = answers.copy()

    def get_dict(self) -> dict:
        return {
            "passage": self.passage,
            "questions": self.questions,
            "answers": self.answers
        }
