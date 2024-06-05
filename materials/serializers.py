from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Serializer for the Course model"""
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    """Serializer for Lessons"""
    class Meta:
        model = Lesson
        fields = '__all__'