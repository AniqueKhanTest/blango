from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    # path("posts/", post_list, name="api_post_list"),
    # path("posts/<int:pk>/", post_detail, name="api_post_detail"),
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
