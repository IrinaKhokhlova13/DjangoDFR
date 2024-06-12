
from materials.models import Course, Lesson
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from materials.permissions import IsOwnerOrStaff, IsModerator
from materials.serializers import (CourseSerializer, LessonSerializer)



class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course model"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]
        elif self.action == 'create':
            self.permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIViewSet(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class LessonListAPIViewSet(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class LessonDetailAPIViewSet(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class LessonUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class LessonDeleteAPIViewSet(generics.RetrieveDestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class CourseCreateAPIViewSet(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]



class CourseUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff | IsModerator]