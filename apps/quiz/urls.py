from rest_framework.routers import DefaultRouter
from apps.quiz.views import QuizTakeViewSet
from quiz.views import QuizViewSet, QuizMetaViewSet, QuestionViewSet, QuizTakeSerializer

router = DefaultRouter()
router.register("quiz-listing", QuizViewSet, 'quiz_listing')
router.register("quiz-meta", QuizMetaViewSet, 'quiz-meta')
router.register("questions", QuestionViewSet, 'questions')
router.register('quiz-take', QuizTakeViewSet, 'quiz-take')

urlpatterns = router.urls
