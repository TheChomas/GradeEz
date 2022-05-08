class EmailTemplate():
    question_text = ""
    answer_text = ""
    score = 0.0

    def __init__(self, question_text: str, answer_text: str, score: str) -> None:
        self.question_text = question_text
        self.answer_text = answer_text
        self.score = score

    def get_dict(self) -> dict:
        return {
            "question_text": self.question_text,
            "answer_text": self.answer_text,
            "score": self.score
        }
