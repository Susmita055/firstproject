from django import forms
from .models import Document, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'document')