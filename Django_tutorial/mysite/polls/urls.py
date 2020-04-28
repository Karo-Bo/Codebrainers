from django.urls import path

from polls import views

urlpatterns = [
    # /polls/index
    path('index', views.index, name='polls_index'),
]