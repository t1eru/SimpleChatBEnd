from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, RegisterView, CustomTokenObtainPairView, ProfileView

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
