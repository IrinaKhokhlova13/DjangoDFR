from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson
from rest_framework import serializers

class LessonSerializer(ModelSerializer):
    """Serializer for Lessons"""

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """Serializer for the Course model"""

    count_lessons = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    read_only = True

    class Meta:
        model = Course
        fields = ["title", "description", "count_lessons", "lessons"]

    @staticmethod
    def get_count_lessons(obj):
        return Lesson.objects.filter(course=obj).count()
