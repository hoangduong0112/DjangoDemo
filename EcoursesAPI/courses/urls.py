from django.urls import re_path, include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('courses', views.CourseViewSet, basename='courses')
router.register('lessons', views.LessonViewSet, basename='lessons')
router.register('user', views.UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls))
]