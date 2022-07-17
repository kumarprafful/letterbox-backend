from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = router.urls + [
    path('admin/', admin.site.urls),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('users/', include('users.urls')),
    path('campaigns/', include('campaigns.urls')),
    path('newsletter/', include('newsletter.urls')),
]
