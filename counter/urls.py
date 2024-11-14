from django.urls import path
from . import views

urlpatterns = [
    path('increment-visit/', views.increment_visit, name='increment_visit'),
]