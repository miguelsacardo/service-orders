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
    # PATCH AND DESTROY
    path('users/<int:userId>', UserDetailView.as_view()),

    # environment urls
    # POST and GET
    path('environments', EnvironmentRegistrationView.as_view()),
    # PUT and GET
    path('environments/<int:pk>', EnvironmentDetailView.as_view()),

    # patrimony urls
    # POST and GET
    path('patrimonies', PatrimonyRegistrationView.as_view()),
    # PUT and GET
    path('patrimonies/<int:pk>', PatrimonyDetailView.as_view()),

    # service orders urls
    # POST and GET
    path('service-orders', ServiceOrderRegistrationView.as_view()),
    # PUT and GET
    path('service-orders/<int:pk>', ServiceOrderDetailView.as_view())

    
]