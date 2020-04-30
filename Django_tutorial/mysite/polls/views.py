from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Question
from django.utils import timezone

# FBV - Function - Based - View
# /polls/index
def index(request):
    results = Question.objects.all()
    # results = Question.objects.none() - pusta lista
    # results = Question.objects.filter(pub_date__gt=timezone.now())
    return render(
        request, "polls/index.html", 
    {
        'title': 'List of questions',
        'question_list': results,
        },
    )

# CBV - Class - Based - View


# MVC - Model View Controler = MTV - Model Template View


# CRUD Create Read Update Delete views
# List - nasz widok index - lista obiektów
# stworzymy widok Read - szczegóły konkretnego obiektu

def details(request, question_id):
    # result = Question.objects.get(id=question_id) # zwraca dokładnie 1 wynik
    result = get_object_or_404(Question, id=question_id)
    return render(
        request, "polls/details.html", 
    {
        'title': f'Question {result.id}',
        'question': result,
        },
    )