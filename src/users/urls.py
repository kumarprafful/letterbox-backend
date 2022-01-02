from rest_framework.routers import DefaultRouter
from django.urls import path
from users import views

router = DefaultRouter()

router.register('auth', views.AuthViewset, 'auth')

urlpatterns = router.urls + [
]
