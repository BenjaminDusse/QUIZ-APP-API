from django.contrib import admin
from quiz.models import *


admin.site.register(Quiz)
admin.site.register(QuizMeta)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTake)
admin.site.register(TakeAnswer)
