from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from main import views as cinema_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/movies/', cinema_views.CinemaListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', cinema_views.CinemaDetailAPIView.as_view()),
    path('api/v1/registration/', user_views.RegistrationAPIView.as_view()),
    path('api/v1/sign_in/', user_views.LoginAPIView.as_view()),
]
