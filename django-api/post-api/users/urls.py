from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('', include(router.urls))
]