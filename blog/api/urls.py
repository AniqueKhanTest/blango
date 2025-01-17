from django.urls import path,include
from .views import PostViewSet,TagViewSet,UserDetail,schema_view
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as drf_auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register("tags",TagViewSet)
router.register("posts",PostViewSet)

urlpatterns = [
    # Function Based
    # path("posts/", post_list, name="api_post_list"),
    # path("posts/<int:pk>/", post_detail, name="api_post_detail"),

    # Custom
    # path("posts/", PostList.as_view(), name="api_post_list"),
    # path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),

    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    
]

urlpatterns+=[
    path("",include(router.urls)),
    path("posts/by-time/<str:period_name>/",PostViewSet.as_view({"get": "list"}),name="posts-by-time",),
    path("swagger/",schema_view.with_ui("swagger",cache_timeout=0),name="schema_swagger_ui"),
    path("token-auth/", drf_auth_views.obtain_auth_token),
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("auth/", include("rest_framework.urls")),
]