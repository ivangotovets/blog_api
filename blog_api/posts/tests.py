from django.db import models
from django.shortcuts import get_object_or_404
from django.test import TestCase

from .models import Post, User


MODELS_FIELD_TYPES = {
    Post: {
        'title': models.CharField,
        'text': models.TextField,
        'created': models.DateTimeField,
        'updated': models.DateTimeField,
        'author': models.ForeignKey,
    },
}


class TestPosts(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create(username='user')
        cls.post = Post.objects.create(
            author=cls.user,
            title='Тест',
            text='Тестовый текст',
        )

    @staticmethod
    def object_data_eq_fixture(object, fixture):
        flag = True
        for field in object.fields:
            if object[field].initial != fixture[field].initial:
                flag = False
        return flag

    def test_post_model_has_correct_fields(self):
        """Создана модель Post с правильными полями."""
        for model, mapping in MODELS_FIELD_TYPES.items():
            for field, field_type in mapping.items():
                with self.subTest(field=field):
                    self.assertIsInstance(
                        model._meta.get_field(field),
                        field_type
                    )

    def test_post_data_equals_fixture(self):
        """Пост совпадает с фикстурой."""
        post = get_object_or_404(Post, id=self.post.id)
        self.assertTrue(post, self.post)
