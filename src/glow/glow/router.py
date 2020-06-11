from api.viewsets import UserViewSet, BlogViewSet, CommentViewSet
from rest_framework import routers

#router
router= routers.DefaultRouter()
#register view sets
router.register('Comment', CommentViewSet, basename="comment")
router.register('User', UserViewSet)
router.register('Blog', BlogViewSet, basename="blog")

