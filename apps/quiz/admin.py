from django.contrib import admin

from quiz.models import Question, Answer_single, Answer_selection


admin.site.register(Question)
admin.site.register(Answer_single)
admin.site.register(Answer_selection)
