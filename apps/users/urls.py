from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.users.views import UserViewSet

app_name = 'users'

urlpatterns = []

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns += router.urls
