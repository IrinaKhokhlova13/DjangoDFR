from django.urls import path
from rest_framework import routers
from materials.serializers import CourseSerializer, LessonSerializer
from materials.views import (LessonCreateAPIViewSet, LessonListAPIViewSet, LessonDetailAPIViewSet,
                             LessonDeleteAPIViewSet, LessonUpdateAPIViewSet, CourseViewSet)
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name
router = routers.DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
urlpatterns = [
                  path('lessons/create/', LessonCreateAPIViewSet.as_view(), name='lesson-create'),
                  path('lessons/list/', LessonListAPIViewSet.as_view(), name='lesson-list'),
                  path('lessons/<int:pk>/', LessonDetailAPIViewSet.as_view(), name='lesson-detail'),
                  path('lessons/<int:pk>/delete/', LessonDeleteAPIViewSet.as_view(), name='lesson-delete'),
                  path('lessons/<int:pk>/update/', LessonUpdateAPIViewSet.as_view(), name='lesson-update'),
              ] + router.urls
