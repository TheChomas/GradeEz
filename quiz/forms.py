from django.forms import ModelForm, Form
from django.db import models

from quiz.models import Answer, Quiz


class QuizCustomForm(Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop("questions")
        super(QuizCustomForm, self).__init__(*args, **kwargs)
        # dynamic fields here ...
        for question in questions:
            self.fields[f'{question.id}'] = models.TextField()


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'parent_question']
        exclude = ['answer_timestamp', 'author', 'score']
