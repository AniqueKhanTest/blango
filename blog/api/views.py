# from http import HTTPStatus
# from django.urls import reverse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from ..serializers import PostSerializer,PostDetailSerializer
from ..models import Post
from .serializers import UserSerializer
from .permissions import AuthorModifyOrReadOnly,IsAdminUserForObject
from blango_auth.models import User
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
    permission_classes = [AuthorModifyOrReadOnly|IsAdminUserForObject]
    serializer_class = PostDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.permissions import BasePermission, SAFE_METHODS

# Q2
# class InversePermissions(BasePermission):
#     # Question 2: Implement your permission methods
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return not request.user.is_anonymous

#         return request.user.is_anonymous

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return not request.user.is_anonymous

#         return request.user.is_anonymous


#Q3
# def create(self, validated_data):
#         address_dict = validated_data.pop("address")
#         address = Address.objects.get_or_create(**address_dict)[0]
#         validated_data["address"] = address
#         return super(CustomerSerializer, self).create(validated_data)


#     def update(self, instance, validated_data):
#         address_dict = validated_data.pop("address")
#         super(CustomerSerializer, self).update(instance, validated_data)

#         if (
#             instance.address.street_name != address_dict["street_name"]
#             or instance.address.city != address_dict["city"]
#         ):
#             address = Address.objects.get_or_create(**address_dict)[0]
#             instance.address = address
#             instance.save()

#         return instance