from django.urls import path,include,re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.authtoken import views as drf_auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version = "v1",
        description="API for Blango Blog"
    ),
    url = "http://localhost:8000/api/",
    public=True
)

urlpatterns = [
    # path("posts/", post_list, name="api_post_list"),
    # path("posts/<int:pk>/", post_detail, name="api_post_detail"),

    # Custom
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),

    # Default
    path("token-auth/", drf_auth_views.obtain_auth_token),
    path("auth/", include("rest_framework.urls")),
    # re_path(
    #     r"^swagger(?P<format>\.json|\.yaml)$",
    #     schema_view.without_ui(cache_timeout=0),
    #     name="schema_json"
    # ),
    path("swagger/",schema_view.with_ui("swagger",cache_timeout=0),name="schema_swagger_ui")
]


urlpatterns = format_suffix_patterns(urlpatterns)

