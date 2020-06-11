import datetime
from django.utils import timezone
from .models import Blog, Comment
from .serializers import BlogSerializer, UserSerializer, CommentSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

#user model viewset
class CommentViewSet(viewsets.ViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	
	#create comment
	def create(self, request, *args, **kwargs):
		requested = request.data
		requested= Comment.objects.create(
			user=request.user,
			content= requested["content"]
			)
		requested.save()
		serializer= CommentSerializer(requested)
		return Response(serializer.data)
	
	#list all comment
	def list(self, request):
		queryset = Comment.objects.all()
		serializer = CommentSerializer(queryset, many=True)
		return Response(serializer.data)

	#retrieve a single comment 
	def retrieve(self, request, pk=None):
		queryset = Comment.objects.all()
		comment = get_object_or_404(queryset, pk=pk)
		serializer = CommentSerializer(comment)
		return Response(serializer.data)

	def destroy(self, request, pk=None):
		if request.user.is_staff:
			Comment.objects.filter(pk=pk).delete()
			return Response("delete successful")
		return Response("YOU ARE NOT AN ADMIN")


# Blog viewset
class BlogViewSet(viewsets.ViewSet):
	#blog queryset
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

	def create(self, request, *args, **kwargs):
		requested = request.data
		if request.user.is_staff:
			requested= Blog.objects.create(
				user=request.user,
				title= requested["title"],
				content= requested["content"]
				)
			requested.save()
			serializer= BlogSerializer(requested)
			return Response(serializer.data)
		return Response("Access denied: You are not an admin")

	#update blog post 
	def update(self, request,pk=None, *args, **kwargs):
		queryset = Blog.objects.all()
		#get post that needs to be updated
		obj = get_object_or_404(queryset, pk=pk)
		requested = request.data
		obj.title=requested["title"]
		obj.content= requested["content"]
		obj.modified_date= timezone.localtime(timezone.now())
		obj.save()
		serializer= BlogSerializer(obj)
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

	def destroy(self, request, pk=None):
		if request.user.is_staff:
			Blog.objects.filter(pk=pk).delete()
			return Response("delete successful")
		return Response("Access denied: You are not an admin")

#user model viewset
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer