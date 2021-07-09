from django.contrib import admin
from django.urls import path
from .views import index, generatePdf

urlpatterns = [
    path('', index, name='index'),

    # api
    path('api/<int:id>', generatePdf.as_view(), name='pdf')
]
