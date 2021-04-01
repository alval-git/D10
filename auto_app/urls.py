from django.contrib import admin
from django.urls import path
from auto_app.views import CarListView

urlpatterns = [
    path('index/', CarListView.as_view()),
]