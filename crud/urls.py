from django.urls import path
from .views import RegisterView,Overview,LoginView,UserView,LogoutView,ProfileView
urlpatterns = [
    path('',Overview.as_view(),name = 'api-overview'),
    path('register/',RegisterView.as_view(),name = 'create-user'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('user/',UserView.as_view(),name = 'user'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('user/<int:pk>/profile/', ProfileView.as_view())

]