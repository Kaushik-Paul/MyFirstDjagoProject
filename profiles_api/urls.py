from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-world/', views.HelloApiView.as_view()),
]