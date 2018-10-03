from django.conf.urls import url, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'goals', GoalView)
router.register(r'actions', ActionView)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]