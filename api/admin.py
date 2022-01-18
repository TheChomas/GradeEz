from django.contrib import admin
from .models import Passage, Question, Student, Answer

# Register your models here.

admin.site.register(Passage)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Answer)
