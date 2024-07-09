from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def test_post_content(self):
        Post.objects.create(title="Test Post", content="Test Content")
        post = Post.objects.get(title="Test Post")
        expected = f'{post.content}'
        self.assertEqual(expected, "Test Content")


class HelloWorldViewTest(TestCase):
    def test_hello_world_view(self):
        response = self.client.get(reverse('hello_world'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World')
