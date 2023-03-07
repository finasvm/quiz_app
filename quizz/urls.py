from django.urls import path
from . import views

app_name = 'quizz'

urlpatterns = [

    path('', views.index,name="index"),
    path('select-question-count/', views.select_question_count,name="select_question_count"),
    path('questions/<str:count>/', views.questions,name="questions"),
    path('result/', views.result,name="result"),

    path("answer-check/<str:id>/",views.answer_check,name="answer_check")

]