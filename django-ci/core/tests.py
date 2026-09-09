from django.core.exceptions import ValidationError
from django.test import TestCase
from products.models import Note


class NoteModelTest(TestCase):

    def test_note_creation(self):
        note = Note.objects.create(
            title="Тестовая заметка",
            text="Текст тестовой заметки"
        )
        self.assertEqual(note.title, "Тестовая заметка")
        self.assertEqual(note.text, "Текст тестовой заметки")
        self.assertIsNotNone(note.created_at)

    def test_title_is_required(self):
        note = Note(title="", text="Текст без названия")
        with self.assertRaises(ValidationError):
            note.full_clean()

    def test_note_exists_in_db(self):
        initial_count = Note.objects.count()
        Note.objects.create(title="Заметка 2", text="Текст 2")
        self.assertEqual(Note.objects.count(), initial_count + 1)