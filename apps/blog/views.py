from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination
from apps.category.models import Category
from django.db.models.query_utils import Q

# Create your views here.

class BlogListView(APIView):
    def get(self, request, format=None):
        if Post.postobjects.all().exists():
            posts = Post.postobjects.all()
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(results, many=True)
            return paginator.get_paginated_response({
                'posts': serializer.data,})
        else:
            return Response({'error': 'No posts found'} ,status=status.HTTP_404_NOT_FOUND)

class PostDetailView(APIView):
    def get(self, request, post_slug, format=None):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)   
        return Response({'post': serializer.data}, status=status.HTTP_200_OK)
    
class BlogListCategoryView(APIView):
    def get(self, request, category_id, format=None):
        if Post.postobjects.all().exists():
            category = Category.objects.get(id=category_id)
            posts = Post.postobjects.filter(category=category)
            paginator = SmallSetPagination()
            result = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(result, many=True)

            return paginator.get_paginated_response({'posts': serializer.data})

        else:
            return Response({'error': 'No posts found'} ,status=status.HTTP_404_NOT_FOUND)
        

class SearchBlogView(APIView):
    def get(self, request, search_term):
        matches = Post.postobjects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(category__name__icontains=search_term))

        paginator = MediumSetPagination()
        serializer = PostSerializer(matches, many=True)
        return Response({'filtered_posts':serializer.data},status=status.HTTP_200_OK)