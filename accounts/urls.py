
from django.urls import path

from accounts.views import AdminCreateView,UserCreateView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    # route to admin creation view
    path("admin/",AdminCreateView.as_view()),

    # route to user creation view
    path("user/",UserCreateView.as_view()),

    # route to token authentication
    path("token/",ObtainAuthToken.as_view()),
]