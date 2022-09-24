import django_filters
from quiz.models import Question

class QuestionFilter(django_filters.FilterSet):
    question_type = django_filters.CharFilter('question_type', 'exact')

    class Meta:
        model = Question
        fields = {
            'id': ['exact'],
            'quiz': ['exact'],
            'question_type': ['exact']
        }