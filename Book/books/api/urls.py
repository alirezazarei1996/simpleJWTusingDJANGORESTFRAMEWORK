from django.urls import path, include
# from .views import BookRudView, BookListView, BookCreateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .routers import router

app_name = 'books'

urlpatterns = [
    path('get-token/', obtain_jwt_token, name='get-token'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token'),
    # path('books/<int:pk>/', BookRudView.as_view(), name='book-retrieve-delete'),
    # path('books/<int:pk>/update/', BookRudView.as_view(), name='book-update'),
    # path('books/create/', BookCreateView.as_view(), name='book-create'),
    # path('books/list/', BookListView.as_view(), name='book-list'),
    path('', include(router.urls)),
]