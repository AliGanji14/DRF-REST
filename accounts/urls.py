from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('api-token-auth/', auth_views.obtain_auth_token),
]
