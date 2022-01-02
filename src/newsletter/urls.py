from django.urls import path
from rest_framework.routers import DefaultRouter

from newsletter import views

router = DefaultRouter()

router.register('genres', views.GenreViewSet, 'genres')
router.register('my-newsletter', views.NewsletterViewSet, 'newsletter')



urlpatterns = router.urls + [
]
