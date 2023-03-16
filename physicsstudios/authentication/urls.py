from django.urls import path, re_path, include

# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import RegisterStudentView, LoginView, UserView

schema_view = get_schema_view(
    openapi.Info(
        title="Authentication Microservice",
        default_version='v1',
        contact=openapi.Contact(email="vikumdabare@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('reswagger/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('register/student/', RegisterStudentView.as_view()),
    path('token/', LoginView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('user/', UserView.as_view()),

]
