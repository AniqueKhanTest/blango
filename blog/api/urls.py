from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.authtoken import views as drf_auth_views

urlpatterns = [
    # path("posts/", post_list, name="api_post_list"),
    # path("posts/<int:pk>/", post_detail, name="api_post_detail"),
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
    path("token-auth/", drf_auth_views.obtain_auth_token),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]
urlpatterns += [
    path("auth/", include("rest_framework.urls")),
]
urlpatterns = format_suffix_patterns(urlpatterns)

