from django.urls import path
from .views import Login, Register, UserAddView, Logout, RegisterView, ObtainAuthToken
from rest_framework.authtoken import views

app_name = 'account'

urlpatterns = [
    path('login', Login.as_view(), name='login_page'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register_page'),
    path('api/user/add', UserAddView.as_view(), name='UserAdd_api'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/authentication', views.obtain_auth_token, name='Api_Auth'),
    path('api/token/', ObtainAuthToken.as_view(), name='api_token_auth')

]
