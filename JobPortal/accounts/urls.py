from django.urls import path
from . import views

urlpatterns = [
    
    # --------------------------- Accounts ----------------------------------------
    path('register/', views.UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', views.UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='user-logout'),
    path('refresh-token/', views.TokenRefreshView.as_view(), name='token-refresh'),
]
