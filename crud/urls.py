from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView,Overview,LoginView,UserView,LogoutView
urlpatterns = [
    path('',Overview.as_view(),name = 'api-overview'),
    path('register/',RegisterView.as_view(),name = 'create-user'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('user/',UserView.as_view(),name = 'user'),
    path('user/<int:pk>/',UserView.as_view(),name = 'user-update'),
    path('logout/',LogoutView.as_view(),name = 'logout'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)