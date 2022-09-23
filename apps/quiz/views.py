from rest_framework.viewsets import ModelViewSet
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

