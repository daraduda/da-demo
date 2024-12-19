from django.contrib import admin
from django.urls import path, include, re_path

from web.views import CarAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/carlist', CarAPIView.as_view()),
    path('api/v1/car/<int:pk>', CarAPIView.as_view()),
]
