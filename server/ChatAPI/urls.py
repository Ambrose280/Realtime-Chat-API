# samsung URL Configuration
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from user import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    
	openapi.Info(
        title='ChatAPI By Ifiok Ambrose',
        default_version='v1',
        description='This is A RestFul API for Real Time Chatting',
        terms_of_service='https://www.github.com/Ambrose280/ChatAPP',
        contact=openapi.Contact(email='ifiokambrose@gmail.com'),
        license=openapi.License(name='Test License')
               ),
        
	public=True,
    # permission_classes=(permissions.IsAuthenticated),

)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/', include('chat.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
