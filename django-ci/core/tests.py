from django.test import TestCase
from core.models import Product


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
    def created_at(self):
        return "12:00"

    def Test_1(self):
        self.assertEqual(self.title, "тест заметка")
        self.assertEqual(self.text, "тест заметка")
        self.assertEqual(self.created_at(), "12:00")