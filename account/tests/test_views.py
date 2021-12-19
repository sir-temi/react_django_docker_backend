from django.test import TestCase
from django.urls import reverse

from account.models import TodoList


class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        works = ['Dance', 'Jump', 'Walk', 'Read', 'Eat']
        for todo in works:
            TodoList.objects.create(
                work=todo
            )
        cls.todo_list = TodoList.objects.all()

    def test_delete_view_url_exists(self):
        url = reverse('account:delete_todo', kwargs={'pk': 3})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.todo_list), 4)

    def test_list_view_url_exists(self):
        url = reverse('account:get_todos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.todo_list), 5)

    def test_add_view_url_exists(self):
        url = reverse('account:add_todo')
        response = self.client.post(url, {'result': 'Move', 'save': True})
        self.assertEqual(response.status_code, 201)

    def test_add_to_view_no_save_attribute_with_string(self):
        url = reverse('account:add_todo')
        response = self.client.post(url, {'result': 'Move'})
        self.assertEqual(response.data, "This is not a number")

    def test_add_to_view_no_save_attribute_with_int(self):
        url = reverse('account:add_todo')
        response = self.client.post(url, {'result': 5})
        self.assertEqual(response.data, 50)
