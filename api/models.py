from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

from utils.datetime_utils import datetime_now_plus_minutes


class Passage(models.Model):
    passage_title = models.TextField(default="")
    passage_text = models.TextField(max_length=7000)

    def __str__(self):
        return self.passage_text.split('.')[0]


class Question(models.Model):
    question_text = models.TextField(max_length=500)
    parent_passage = models.ForeignKey(Passage, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.TextField(max_length=1000)
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    score = models.IntegerField(default=-1)

    def __str__(self):
        return self.answer_text


class Test(models.Model):
    test_title = models.TextField(default="")
    test_description = models.TextField(max_length=7000)

    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime_now_plus_minutes)

    passage = models.ManyToManyField(Passage)

    def __str__(self):
        return self.test_title
