from django.urls import path, include
from diary import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('scripts', views.DiaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('deleteAll', views.deleteAllDiary),

]