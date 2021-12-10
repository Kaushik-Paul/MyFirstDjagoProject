from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-world/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
