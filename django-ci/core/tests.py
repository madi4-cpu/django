from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Note

class NoteModelTest(TestCase):

    def test_note_creation(self):
        note = Note.objects.create(title="Тестовая заметка", text="Текст заметки")
        self.assertEqual(note.title, "Тестовая заметка")
        self.assertEqual(note.text, "Текст заметки")

    def test_title_is_required(self):
        note = Note(title="", text="Без названия")
        with self.assertRaises(ValidationError):
            note.full_clean()

    def test_note_saved_in_db(self):
        Note.objects.create(title="Заметка в БД", text="Проверка записи")
        self.assertEqual(Note.objects.count(), 1)