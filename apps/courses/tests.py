from rest_framework import status
from rest_framework.test import APITestCase

from apps.courses.models import Course, Lesson, Subscription, Payment
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


class CourseTestCase(APITestCase):
    """BEFORE TEST CHANGE PERMISSIONS IN apps/courses/views/course"""

    def setUp(self) -> None:
        self.url = '/courses/courses/'
        self.user = User.objects.create(email='test@example.com', password='test')
        self.data = {
            'course_name': 'test',
            'owner': self.user
        }

        self.course = Course.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_course(self):
        """Course creation testing """
        data = {
            'course_name': 'test',
            'owner': self.user.pk
        }
        response = self.client.post(f'{self.url}', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Course.objects.all().count(), 2)

    def test_2_list_course(self):
        """Course list testing """
        response = self.client.get(f'{self.url}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['results'],
            [{'course_name': 'test', 'preview': None, 'description': None, 'lesson_count': 0, 'lesson': [],
              'subscription': False}]
        )

    def test_3_retrieve_course(self):
        """Course retrieve testing """

        response = self.client.get(f'{self.url}{self.course.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'course_name': 'test', 'preview': None, 'description': None, 'lesson_count': 0, 'lesson': [],
             'subscription': False}
        )

    def test_4_update_course(self):
        """Course update testing """
        data = {
            'course_name': 'test2',
            'owner': self.user.pk
        }

        response = self.client.put(f'{self.url}{self.course.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'course_name': 'test2', 'preview': None, 'description': None, 'lesson_count': 0, 'lesson': [],
             'subscription': False}
        )

    def test_5_update_partial_course(self):
        """Course partial update testing """
        data = {
            'course_name': 'test2'
        }
        response = self.client.patch(f'{self.url}{self.course.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'course_name': 'test2', 'preview': None, 'description': None, 'lesson_count': 0, 'lesson': [],
             'subscription': False}
        )

    def test_6_destroy_course(self):
        """Course destroying testing """
        response = self.client.delete(f'{self.url}{self.course.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Course.objects.all().exists())


class PaymentTestCase(APITestCase):
    """BEFORE TEST CHANGE PERMISSIONS IN apps/courses/views/payment"""

    def setUp(self) -> None:
        self.url = '/courses/'
        self.user = User.objects.create(email='test@example.com', password='test')
        self.data = {
            'user': self.user,
            'sum': 10_000,
            'method': 'cash'
        }

        self.payment = Payment.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_list_payment(self):
        """Payment list testing """
        response = self.client.get(f'{self.url}payments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.payment.pk, 'course': None, 'lesson': None,
              'payment_date': f'{str(self.payment.payment_date)[:10]}T{str(self.payment.payment_date)[11:-6]}Z',
              'sum': 10000,
              'method': 'cash', 'user': 14}]
        )

    def test_2_retrieve_payment(self):
        """Payment retrieve testing """

        response = self.client.get(f'{self.url}payment/{self.payment.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.payment.pk, 'course': None, 'lesson': None,
             'payment_date': f'{str(self.payment.payment_date)[:10]}T{str(self.payment.payment_date)[11:-6]}Z',
             'sum': 10000,
             'method': 'cash', 'user': 15}
        )

        def tearDown(self):
            User.objects.all().delete()
