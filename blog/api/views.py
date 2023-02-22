from ..models import Post,Tag
from .serializers import PostDetailSerializer,PostSerializer,UserSerializer,TagSerializer
from .permissions import AuthorModifyOrReadOnly,IsAdminUserForObject
from blango_auth.models import User
from rest_framework import generics,viewsets
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.throttling import ScopedRateThrottle
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.http import Http404

## Class Based Views

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version = "v1",
        description="API for Blango Blog"
    ),
    url = "http://localhost:8000/api/",
    public=True
)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [AuthorModifyOrReadOnly|IsAdminUserForObject]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "post_api"

    def get_serializer_class(self):
        if self.action in ("list","create"):
            return PostSerializer
        return PostDetailSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            # published only
            queryset= self.queryset.filter(published_at__lte=timezone.now())

        elif not self.request.user.is_staff:
            #allow all
            queryset= self.queryset
        
        # filter for own and published
        else:
            queryset= self.queryset.filter(Q(published_at__lte=timezone.now())|Q(author=self.request.user))

        time_period_name = self.kwargs.get("period_name")
        if not time_period_name:
            return queryset
        if time_period_name == "new":
            return queryset.filter(published_at__lte=timezone.now()-timedelta(hours=1))
        elif time_period_name == "today":
            return queryset.filter(published_at__date=timezone.now().date())
        elif time_period_name == "week":
            return queryset.filter(published_at__gte=timezone.now()-timedelta(days=7))
        else:
            raise Http404(f"Time period {time_period_name} is not valid, show be 'new','today' or 'week'")
        
    
    
    
    
    @method_decorator(cache_page(120))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def list(self,*args,**kwargs):
        return super(PostViewSet,self).list(*args,**kwargs)

    @method_decorator(cache_page(300))
    @method_decorator(vary_on_headers("Authorization","Cookie"))
    @action(methods=['get'],detail=False,name="Posts by the current logged in user")
    def mine(self,request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in the see which Posts are yours")
        posts = self.get_queryset().filter(author=request.user)
        serializer = PostSerializer(posts,many=True,context={"request":request})
        return Response(serializer.data)


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "user_api"

    @method_decorator(cache_page(300))
    def get(self,*args,**kwargs):
        return super(UserDetail,self).get(*args,**kwargs)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['get'],detail=True,name='Posts with the Tag')
    def posts(self,request,pk=None):
        tag = self.get_object()
        post_serializer = PostSerializer(tag.posts,many=True,context={"request":request})
        return Response(post_serializer.data)

    @method_decorator(cache_page(300))
    def list(self, *args, **kwargs):
        return super(TagViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super(TagViewSet, self).retrieve(*args, **kwargs)



# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     permission_classes = [AuthorModifyOrReadOnly|IsAdminUserForObject]
#     serializer_class = PostDetailSerializer



# from http import HTTPStatus
# from django.urls import reverse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response    



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