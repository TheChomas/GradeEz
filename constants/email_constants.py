
EMAIL_BODY_TEMPLATE = '''

'''


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
