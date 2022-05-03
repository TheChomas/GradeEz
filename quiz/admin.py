from django.contrib import admin
from .models import Passage, Question, Answer, Quiz

# Register your models here.

admin.site.register(Passage)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)