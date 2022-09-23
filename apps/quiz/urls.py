from django.urls import path
from rest_framework.routers import DefaultRouter
from quiz.views import QuizViewSet, QuizMetaViewSet, QuestionViewSet

router = DefaultRouter()
router.register("quiz-listing", QuizViewSet, 'quiz_listing')
router.register("quiz-meta", QuizMetaViewSet, 'quiz-meta')
router.register("questions", )

urlpatterns = router.urls
