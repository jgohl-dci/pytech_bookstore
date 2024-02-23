from django.test import TestCase
from store.forms import ContactForm, BookForm, AuthorForm
from django import forms


class TestAuthorModel(TestCase):

    def test_message_field_widget(self):
        form = ContactForm()
        widget = form.fields['message'].widget
        self.assertIsInstance(widget, forms.Textarea())
