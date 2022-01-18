from django.db import models
from django.utils import timezone


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


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_usn = models.CharField(max_length=15)
    student_sem = models.IntegerField()
    student_section = models.CharField(max_length=1)

    def __str__(self):
        return self.student_name


class Answer(models.Model):
    answer_text = models.TextField(max_length=1000)
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text
