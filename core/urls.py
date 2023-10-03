from __future__ import annotations

from django.urls import path

from core.views import HomeView
from core.views import template1


urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('report/', template1, name='report'),
]
