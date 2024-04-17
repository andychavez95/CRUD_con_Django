from django import forms
from Libreria.models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'