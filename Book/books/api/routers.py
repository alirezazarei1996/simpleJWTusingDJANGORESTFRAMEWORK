from rest_framework import routers
from .views import BookLCRUDViewSet

router = routers.SimpleRouter()

router.register('books', BookLCRUDViewSet)