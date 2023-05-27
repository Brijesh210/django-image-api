from django.urls import path, include
from rest_framework import routers

from imageapp.api import views

router = routers.DefaultRouter()
router.register('images', views.ImageViewSet)
router.register('tier_sizes', views.SizedTierViewSet)
router.register('image_sizes', views.SizedImageViewSet)
router.register('tiers', views.TierViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('/', include(router.urls))
]
