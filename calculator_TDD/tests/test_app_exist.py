from unittest import TestCase

from calculator import Calculator


class AppExistTest(TestCase):
    def test_app_exist(self):
        self.assertIsNotNone(Calculator)