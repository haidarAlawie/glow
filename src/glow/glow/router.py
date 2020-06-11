from api.viewsets import UserViewSet, BlogViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register('User', UserViewSet)
router.register('Blog', BlogViewSet, basename="blog")
