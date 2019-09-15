from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from books.models import Book
from .serializers import BookSerializer
# from rest_framework.permissions import IsAuthenticated

class BookLCRUDViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a Book instance.

    list:
        Return all Books.

    create:
        Create a new Book.

    delete:
        Remove an existing Book.

    partial_update:
        Update one or more fields on an existing Book.

    update:
        Update a Book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JSONWebTokenAuthentication, ]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    # permission_classes = [IsAuthenticated, ]
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

# class BookCreateView(generics.CreateAPIView): # Because of look_up field we can't mixin create view in RUD view!
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)

# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer