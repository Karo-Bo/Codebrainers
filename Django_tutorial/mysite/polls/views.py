from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.utils import timezone

# FBV - Function - Based - View
# /polls/index
def index(request):
    results = Question.objects.filter(pub_date__lt = timezone.now())
    
    return HttpResponse(', '.join([str(x) for x in results]))

# CBV - Class - Based - View
# MVC - Model View Controler = MTV - Model Template View
