from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from quiz.models import *
from quiz.serializers import *


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    ordering = ["title", "meta_title"]

    def get_serializer_class(self):
        if self.action == "list":
            return QuizListSerializer
        if self.action == "detail":
            return QuizSerializer
        return super().get_serializer_class()


class QuizMetaViewSet(ModelViewSet):

    queryset = QuizMeta.objects.all()
    serializer_class = QuizMetaSerializer
    

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.select_related("quiz")
    serializer_class = QuestionSerializer
    ordering = ["question_type"]
    filter_backends = [DjangoFilterBackend]

class QuizTakeViewSet(ModelViewSet):
    queryset = QuizTake.objects.select_related("quiz")
    serializer_class = QuizTakeSerializer
    ordering = ["id"]
