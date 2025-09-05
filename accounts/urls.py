from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import UserModelViewSet



urlpatterns = [
    path ('user/', UserModelViewSet.as_view (), name= 'User'),
    path ('api/token/obtain/', TokenObtainPairView.as_view(), name= 'Token_Obtain'),
    path ('api/token/refresh/', TokenRefreshView.as_view(), name= 'Token_Refresh'),
    
]
