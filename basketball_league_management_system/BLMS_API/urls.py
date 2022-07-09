from django.urls import path
from django.conf.urls import include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello", views.HelloViewSet, basename="hello")

urlpatterns = [
    path('hello-api/', views.HelloApiView.as_view(), name='My_API'),
]+router.urls
