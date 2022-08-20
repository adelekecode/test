from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/login/', views.login_view, name='login'),
    path('auth/', include('djoser.urls')),
    path("auth/logout/", views.logout_view, name="logout_view"),
    path('auth/refresh/', TokenRefreshView().as_view(), name="refresh_token"),
    ]

    