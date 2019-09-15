from django.urls import path, include
# from .views import BookRudView, BookListView, BookCreateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .routers import router
from rest_framework.schemas import get_schema_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(
    title='Users API', 
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer], 
    authentication_classes=[SessionAuthentication, BasicAuthentication])

app_name = 'books'

urlpatterns = [
    path('get-token/', obtain_jwt_token, name='get-token'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token'),
    # path('books/<int:pk>/', BookRudView.as_view(), name='book-retrieve-delete'),
    # path('books/<int:pk>/update/', BookRudView.as_view(), name='book-update'),
    # path('books/create/', BookCreateView.as_view(), name='book-create'),
    # path('books/list/', BookListView.as_view(), name='book-list'),
    path('docs/', schema_view, name='api-docs'),
    path('', include(router.urls)),
]