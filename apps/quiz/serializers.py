# from rest_framework.serializers import ModelSerializer
# from quiz.models import Category, Question, AnswerSingle, AnswerChoice


# class CategorySerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["id", "label", "featured_question"]


# class AnswerSingleSerializer(ModelSerializer):
#     class Meta:
#         model = AnswerSingle
#         fields = ["id", "content", "is_correct", "draft", "question"]


# class AnswerChoiceSerializer(ModelSerializer):
#     class Meta:
#         model = AnswerChoice
#         fields = ["id", "content", "is_correct", "question", "user_answer"]


# class QuestionSerializer(ModelSerializer):
#     answer_single = AnswerSingleSerializer()
#     answer_choice = AnswerChoiceSerializer()

#     class Meta:
#         model = Question
#         fields = ["id", "answer_single", "answer_choice", "draft"]
