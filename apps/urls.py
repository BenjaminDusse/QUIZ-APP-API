from django.urls import path, include


urlpatterns = [
    path("quizzes/", include(("quiz.urls", 'quizzes'), 'quizzes')),
    
]