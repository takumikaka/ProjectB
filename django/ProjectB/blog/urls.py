# -*- coding: utf-8 -*-

from django.urls import path
from  . import views

urlpatterns = [
            path(r'', views.dy, name='dy'),
            path(r'<int:article_id>/', views.dy_detail, name='dy_detail'),
]
