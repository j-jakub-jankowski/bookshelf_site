from rest_framework import routers

from book_management.viewsets import BookViewSet

router = routers.DefaultRouter()
router.register('book', BookViewSet)
