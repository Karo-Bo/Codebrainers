from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from polls.models import Question, Choice
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
        'choices_filtered': result.choice_set.filter(choice_text__icontains='a'),
        },
    )

    # icontains - case insensitive

def vote(request, question_id):
    # 1. widok musi sprawdzić, czy to jest żądanie POST
    # 2. odczytać dane POST
    # 3. sprawdzić poprawność danych POST/ walidacja pola
    # 4. lista akcji: 
    #   - oddanie głosu na dany wybór
    #   (- wyświetlić komunikat o zagłosowaniu poprawnie)
    #   - przekierować użytkownika
    #
    # jeżeli nie POST -> akcje
    # jeżeli dane POST niepoprawne -> akcje

    if request.method == "POST":
        data = request.POST
        print(data)

        question = get_object_or_404(Question, id=question_id)
        try:
            choice_id = int(data.get('choice', 0)) # 0 jest tutaj domyślną wartością, inaczej - None
            question.choice_set.get(id=choice_id)
        except (ValueError, Choice.DoesNotExist):
            # jeżeli dane POST niepoprawne -> akcje
            pass
        else:
            pass # jeżeli w bloku try żaden z wyjątków nie wystąpi
    else:
        return redirect('https://niebezpiecznik.pl')
