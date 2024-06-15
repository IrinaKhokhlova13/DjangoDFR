from rest_framework.test import APITestCase
from materials.models import Lesson, Course, Subscription
from users.models import User
from rest_framework import status


class LessonsTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        """Тестирование: создание урока"""

        data = {
            'name': 'test_lesson',
            'description': 'test_description',
        }
        response = self.client.post('/school/lessons/create/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_list_lessons(self):
        Lesson.objects.create(name='test_lesson', description='test_description')

        """Тестирование: получение списка уроков"""

        response = self.client.get('/school/lessons/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {'count': 1, 'next': None, 'previous': None, 'results': [
                             {'id': 3, 'name': 'test_lesson', 'description': 'test_description', 'preview_image': None,
                              'video_link': None, 'course': None, 'owner': None}]}
                         )

    def test_update_lesson(self):
        """Тестирование: обновление урока"""

        lesson = Lesson.objects.create(name='test_lesson', description='test_description')
        data = {
            'name': 'test_lesson_updated',
            'description': 'test_description_updated',
        }
        response = self.client.put(f'/school/lessons/{lesson.id}/update/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_lesson(self):
        """Тестирование: удаление урока"""

        lesson = Lesson.objects.create(name='test_lesson', description='test_description')
        response = self.client.delete(f'/school/lessons/{lesson.id}/delete/')
        self.assertEqual(response.status_code, 204)





class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@service.py")
        self.user.set_password('1')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Python_29", owner=self.user)

    def test_subscribe(self):
        data = {
            "course": self.course.pk
        }
        response = self.client.post(
            '/course/subscribe/',
            data=data
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'Подписка включена'})

    def test_unsubscribe(self):
        data = {
            "course": self.course.pk
        }
        Subscription.objects.create(course=self.course, user=self.user)
        response = self.client.post(
            '/course/subscribe/',
            data=data
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'Подписка отключена'})