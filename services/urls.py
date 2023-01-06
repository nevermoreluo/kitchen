"""
Services urlpatterns list routes
"""
from typing import List, Any

from django.urls import path

from . import views

urlpatterns: list[Any] = [
    path('', views.index, name='index'),
]