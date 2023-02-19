# from http import HTTPStatus
# from django.urls import reverse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from ..serializers import PostSerializer
from ..models import Post

# Function based view

# @api_view(["GET", "POST"])
# def post_list(request, format=None):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         return Response({"data": PostSerializer(posts, many=True).data})
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             post = serializer.save()
#             return Response(data=serializer.data, status=HTTPStatus.CREATED,
#                             headers={"Location": reverse("api_post_detail", args=(post.pk,))})
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


# @api_view(['GET', "PUT", "DELETE"])
# def post_detail(request, pk, format=None):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=HTTPStatus.NOT_FOUND)
#     if request.method == 'GET':
#         return Response(PostSerializer(post).data)
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=HTTPStatus.NO_CONTENT)
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=HTTPStatus.NO_CONTENT)


## Class Based Views
## Taking the second approach

from rest_framework import generics

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer