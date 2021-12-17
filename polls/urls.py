from django.urls import path
from . import views
from .views import DeleteView

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('allresults/', views.AllResultView.as_view(), name='allresults'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]