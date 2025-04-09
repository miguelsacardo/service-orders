from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # token urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # user urls
    # POST and GET
    path('users', UserRegistrationView.as_view()),
    # UPDATE AND DESTROY
    path('users/<int:pk>', UserDetailView.as_view()),
    
]