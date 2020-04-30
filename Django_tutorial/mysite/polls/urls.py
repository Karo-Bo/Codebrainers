from django.urls import path

from polls import views

urlpatterns = [
    # /polls/
    path('', views.index, name='polls_index'),
    # /polls/<question_id>
    path('<int:question_id>', views.details, name='polls_details'),
]