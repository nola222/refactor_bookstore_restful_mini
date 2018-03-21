from django.contrib.auth.models import User
from rest_framework import serializers
from books.models import Books

# 使根路由直接可以链接到子路由
class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
