from django.shortcuts import render

# Create your views here.
from books.models import Books
from books.serializers import BooksSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
