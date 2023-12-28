from django.urls import path

from .views import CreateView, UpdateView

urlpatterns = [
    path('create', CreateView.as_view()),
    path('update', UpdateView.as_view())
]
