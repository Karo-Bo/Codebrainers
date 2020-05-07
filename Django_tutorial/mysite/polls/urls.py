from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    # /
    path('', views.index, name='index'), # polls:index
    # /<question_id>
    path('<int:question_id>', views.details, name='details'), # polls:details
    # /<question_id>/vote
    path('<int:question_id>/vote', views.vote, name='vote'), # polls:vote
]