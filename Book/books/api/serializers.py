from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from datetime import date

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'pk',
            'user',
            'title',
            'author',
            'year',
        ]
        read_only_fields = ['pk', 'user']