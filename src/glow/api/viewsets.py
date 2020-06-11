from .models import Blog, Comment
from .serializers import BlogSerializer, UserSerializer, CommentSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer