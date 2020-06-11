from .models import Blog, Comment
from .serializers import BlogSerializer, UserSerializer, CommentSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response


class BlogViewSet(viewsets.ViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	def list(self, request):
		queryset = Blog.objects.all()
		serializer = BlogSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Blog.objects.all()
		blog = get_object_or_404(queryset, pk=pk)
		serializer = BlogSerializer(blog)
		return Response(serializer.data)



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer