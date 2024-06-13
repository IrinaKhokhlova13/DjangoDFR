from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson, Subscription, Payments
from rest_framework import serializers

from materials.validators import LessonsValidator


class LessonSerializer(ModelSerializer):
    """Serializer for Lessons"""

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonsValidator(url="video_link")]


class CourseSerializer(ModelSerializer):
    """Serializer for the Course model"""

    count_lessons = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    read_only = True

    class Meta:
        model = Course
        fields = ["title", "description", "count_lessons", "lessons"]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    @staticmethod
    def get_count_lessons(obj):
        return Lesson.objects.filter(course=obj).count()



class SubscriptionSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели Subscription"""

    class Meta:
        model = Subscription
        fields = "__all__"


class PaymentsSerializer(serializers.Serializer):
    """Класс сериализатора для модели Payments"""

    class Meta:
        model = Payments
        fields = "__all__"