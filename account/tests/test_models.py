from django.test import TestCase

from account.models import TodoList


class ModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo = TodoList.objects.create(
            work="Stroll"
        )

    def test_model_was_created(self):
        self.assertEqual(self.todo.work, "Stroll")

    def test_str_method_on_model(self):
        self.assertEqual(str(self.todo), f"{self.todo.work} in ToDo")
