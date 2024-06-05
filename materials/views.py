
from materials.models import Course, Lesson

from rest_framework import generics, viewsets
from materials.serializers import (CourseSerializer, LessonSerializer)



class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course model"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIViewSet(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIViewSet(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDetailAPIViewSet(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIViewSet(generics.RetrieveDestroyAPIView):
    queryset = Lesson.objects.all()