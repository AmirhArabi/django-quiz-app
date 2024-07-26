from rest_framework.authtoken import views
from django.urls import path
from .views import (Quiz, Result, send_email, QuestionListView,
                    ResultView, CategoryListView,
                    CategoryQuestionList, AnswerView,
                    StartGame, LeaderBoard)

app_name = 'quiz'
urlpatterns = [
    path('', Quiz.as_view(), name='quiz_page'),
    path('result', Result.as_view(), name='result_page'),
    path('receive-result', send_email, name='send_email'),
    path('api/questions', QuestionListView.as_view(), name='questionList_api'),
    path('api/categories', CategoryListView.as_view(), name='categoryList_api'),
    path('api/categories/<str:category_name>/questions', CategoryQuestionList.as_view(), name='category_questions'),
    path('api/game/<str:category_name>/start', StartGame.as_view(), name='category_questions'),
    path('api/userresult', ResultView.as_view(), name='UserResult_api'),
    path('api/game/submit', AnswerView.as_view(), name='submit_answer'),
    path('api/leaderboard', LeaderBoard.as_view(), name='leadr_board')
]
