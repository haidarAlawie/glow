from .models import Blog, Comment
from .serializers import BlogSerializer, UserSerializer, CommentSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# Blog viewset
class BlogViewSet(viewsets.ViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

	def create(self, request, *args, **kwargs):
		requested = request.data
		requested= Blog.objects.create(
			user=request.user,
			title= requested["title"],
			content= requested["content"]
			)
		requested.save()
		serializer= BlogSerializer(requested)
		return Response(serializer.data)
	
	#list all blog posts
	def list(self, request):
		queryset = Blog.objects.all()
		serializer = BlogSerializer(queryset, many=True)
		return Response(serializer.data)

	#retrieve a single blog post 
	def retrieve(self, request, pk=None):
		queryset = Blog.objects.all()
		blog = get_object_or_404(queryset, pk=pk)
		serializer = BlogSerializer(blog)
		return Response(serializer.data)


#user model viewset
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer