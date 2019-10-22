
from django import forms

from app.models import *

class CreateBookForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=100)
    date = forms.DateField(label='Date:')
    authors = forms.MultipleChoiceField(label='Authors:', choices=Author.objects.all().iterator())
    publisher = forms.ChoiceField(label='Publisher:', choices=Publisher.objects.all())