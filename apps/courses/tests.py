from rest_framework import status
from rest_framework.test import APITestCase

from apps.courses.models import Course, Lesson, Subscription
from apps.users.models import User


class LessonTestCase(APITestCase):
    """BEFORE TEST CHANGE PERMISSIONS IN apps/courses/views/lesson"""

    def setUp(self) -> None:
        self.url = '/courses/'
        self.course = Course.objects.create(course_name='test')
        self.user = User.objects.create(email='test@example.com', password='test')
        self.data = {
            'course': self.course,
            'lesson_name': 'test',
            'owner': self.user
        }

        self.lesson = Lesson.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_lesson(self):
        """Lesson creation testing """
        data = {
            'course': self.course,
            'lesson_name': 'test2',
            'owner': self.user.pk
        }
        response = self.client.post(f'{self.url}add_lesson/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_2_list_lesson(self):
        """Lesson list testing """
        response = self.client.get(f'{self.url}lessons/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['results'],
            [{'id': self.lesson.pk, 'course': 'test', 'lesson_name': 'test', 'description': None, 'preview': None,
              'video_link': None, 'owner': self.user.pk}]
        )

    def test_3_retrieve_lesson(self):
        """Lesson retrieve testing """

        response = self.client.get(f'{self.url}lesson/{self.lesson.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'course': 'test', 'lesson_name': 'test', 'description': None, 'preview': None,
             'video_link': None, 'owner': self.user.pk}
        )

    def test_4_update_lesson(self):
        """Lesson update testing """
        data = {
            'course': self.course,
            'lesson_name': 'test2',
            'owner': self.user.pk
        }

        response = self.client.put(f'{self.url}lesson/update/{self.lesson.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'course': 'test', 'lesson_name': 'test2', 'description': None, 'preview': None,
             'video_link': None, 'owner': self.user.pk}
        )

    def test_5_update_partial_lesson(self):
        """Lesson partial update testing """
        data = {
            'lesson_name': 'test2'
        }
        response = self.client.patch(f'{self.url}lesson/update/{self.lesson.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'course': 'test', 'lesson_name': 'test2', 'description': None, 'preview': None,
             'video_link': None, 'owner': self.user.pk}
        )

    def test_6_destroy_lesson(self):
        """Lesson destroying testing """
        response = self.client.delete(f'{self.url}lesson/delete/{self.lesson.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Lesson.objects.all().exists())

    def test_7_create_lesson_validation_error(self):
        """Lesson creation testing with validation error """
        data = {
            'course': self.course,
            'lesson_name': 'test2',
            'owner': self.user.pk,
            'video_link': 'https://stackoverflow.com/questions/16828315/how-can-i-make-my-model-fields-optional-in-django'
        }

        response = self.client.post(f'{self.url}add_lesson/', data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'non_field_errors': ['You can add only youtube videos']}
        )


class SubscriptionTestCase(APITestCase):
    """BEFORE TEST CHANGE PERMISSIONS IN apps/courses/views/subscription"""

    def setUp(self) -> None:
        self.url = '/courses/'
        self.course = Course.objects.create(course_name='test')
        self.user = User.objects.create(email='test@example.com', password='test')
        self.data = {
            'course': self.course,
            'user': self.user
        }

        self.subscription = Subscription.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_subscription(self):
        """Subscription creation testing """
        data = {
            'course': self.course.pk,
            'user': self.user.pk
        }
        response = self.client.post(f'{self.url}add_subscription/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Subscription.objects.all().count(), 2)

    def test_2_destroy_subscription(self):
        """Subscription destroying testing """
        response = self.client.delete(f'{self.url}subscription/delete/{self.subscription.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Subscription.objects.all().exists())
