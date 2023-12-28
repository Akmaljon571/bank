from django.urls import path

from .views import CreditAllViews, CreditOneViews

urlpatterns = [
    path('', CreditAllViews.as_view()),
    path('<int:pk>', CreditOneViews.as_view())
]