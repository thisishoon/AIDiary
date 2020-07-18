from django.urls import path, include
from diary import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]