from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from auth_.views import logout, register, AuthorsListAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('logout/', logout),
    path('register/', register),
    path('authors/', AuthorsListAPIView.as_view())
]
