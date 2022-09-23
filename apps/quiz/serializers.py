from rest_framework.serializers import ModelSerializer
from quiz.models import Quiz, QuizMeta, Question, Answer, QuizTake, TakeAnswer

class QuizListSerializer(ModelSerializer):

    class Meta:
        model = Quiz
        fields = [
            'id', 
            'title', 
            'meta_title',
            'quiz_type',
            'content'
        ]

class QuizSerializer(ModelSerializer):

    class Meta:
        model = Quiz
        fields = [
            'id',
            'host_id',
            'title',
            'meta_title',
            'slug',
            'summary',
            'quiz_type',
            'score',
            'published',
            'starts_at',
            'ends_at',
            'content'
        ]

class QuizMetaSerializer(ModelSerializer):

    class Meta:
        model = QuizMeta
        fields = [
            'id',
            'quiz',
            'content'
        ]

class QuestionListSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'id',
            'quiz',
            'question_type',
            'level',
            'score',
            'content'
        ]

class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'id',
            'quiz',
            'question_type',
            'active',
            'level',
            'score',
            'content'
        ]

class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id',
            'quiz',
            'question',
            'active',
            'correct',
            'content'
        ]


class QuizTakeSerializer(ModelSerializer):

    class Meta:
        fields = [
            'id',
            'user',
            'quiz',
            'status',
            'score',
            'starts_at',
            'finished_at',
            'content'
        ]

class TakeAnswerSerializer(ModelSerializer):

    class Meta:
        model = TakeAnswer
        fields = [
            'id',
            'quiz_take',
            'answer',
            'active',
            'content'
        ]