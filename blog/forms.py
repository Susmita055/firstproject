from django import forms
from django.core.exceptions import FieldDoesNotExist
from django.db.models import fields
from django.forms.models import model_to_dict
from .models import Document, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'document')




class Subscribe(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email


    