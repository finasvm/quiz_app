from django.shortcuts import render, redirect
from .models import Question, UserList, AnswerRecord, Option, AttemptHistory
from django.core.paginator import Paginator
import json
import random
from django.http import JsonResponse


def index(request):
    if request.method == "POST":
        name = request.POST.get('username')
        user = UserList.objects.create(name=name)
        request.session['user_id'] = user.id
        return redirect("quizz:select_question_count")
    return render(request, 'web/index.html')


def select_question_count(request):
    if request.method == "POST":
        number_of_question = request.POST['count']
        user_id = request.session['user_id']
        user = UserList.objects.get(id=user_id)
        attempt = AttemptHistory.objects.create(user=user)
        request.session["attempt_id"] = attempt.id
        return redirect("/questions/"+number_of_question)
    return render(request, 'web/select-question.html')


def questions(request, count):
    question_count = int(count)
    total_options = Question.objects.all()
    question_ids = []
    for op in total_options:
        question_ids.append(op.id)
    selected_question_ids = random.sample(question_ids, question_count)
    options = Question.objects.filter(id__in=selected_question_ids)
    paginator = Paginator(options, 1)
    page_number = request.GET.get('page')
    question = paginator.get_page(page_number)
    context = {
        "question": question,
    }
    return render(request, 'web/questions.html', context)


def answer_check(request, id):
    selected_option = Option.objects.get(id=id)
    question = selected_option.question
    attempt_id = request.session["attempt_id"]
    AnswerRecord.objects.create(
        attempt_id=attempt_id,
        question=question,
        option_selected=selected_option,
        is_correct_option=selected_option.is_answer
    )
    return JsonResponse({
        'status': "success",
        "message": selected_option.is_answer,
        'option': selected_option.id,
    })


def result(request):
    attempt_id = request.session["attempt_id"]
    attempt = AttemptHistory.objects.get(id=attempt_id)
    answer_record = AnswerRecord.objects.filter(attempt=attempt)
    number_of_question = len(answer_record)
    correct_answer = len(answer_record.filter(is_correct_option=True))
    percentage = round(correct_answer * 100 / number_of_question)
    attempt.is_active = False
    attempt.save()
    context = {
        "correct_answer": correct_answer,
        "percentage": percentage,
        "attempt": attempt,
    }
    return render(request, 'web/result.html', context)
