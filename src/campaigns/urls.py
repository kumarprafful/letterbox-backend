from django.urls import path
from rest_framework.routers import DefaultRouter

from campaigns import views

router = DefaultRouter()

router.register('campaign-contents',
                views.ContentViewSet, 'campaign-contents')
# router.register('my-campaign', views.CampaignViewSet, 'my-campaign')
router.register('my-campaign', views.CampaignViewSet, 'my-campaign')


urlpatterns = router.urls + [
    # path('my-campaigns-list', views.CampaignListView.as_view(), name='campaigns'),
    path('set-indexes/', views.set_sequence_of_contents, name='set-indexes'),

]
