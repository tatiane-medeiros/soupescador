from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:pescaria_id>/', views.detail, name='detail'),
]
