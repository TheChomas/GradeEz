from django.contrib import admin
from .models import Passage, Question, Answer, Quiz

# Register your models here.


class PassageAdmin(admin.ModelAdmin):
    search_fields = ['passage_title', 'passage_text']


class QuestionAdmin(admin.ModelAdmin):
    search_fields = [
        'question_text', 'parent_passage__passage_title']


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['answer_text', 'parent_question__question_text',
                     'author__username', 'author__email', 'score']


class QuizAdmin(admin.ModelAdmin):
    search_fields = ['quiz_title', 'quiz_description',
                     'passage__passage_title', 'students__username', 'students__email']


admin.site.register(Passage, PassageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Quiz, QuizAdmin)

# admin stuff
admin.site.site_header = "GradeEz Admin"
admin.site.site_title = "GradeEz Admin Portal"
admin.site.index_title = "Welcome to GradeEz Portal"
