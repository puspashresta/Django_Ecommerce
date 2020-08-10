from django.urls import path, include
from rest_framework import routers

from .views import ItemViewSet, BannerViewSet, ItemFilterListView

router = routers.DefaultRouter()
router.register('item',ItemViewSet)
router.register('banner',BannerViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('item_api',ItemFilterListView.as_view(),name='item_api')
]