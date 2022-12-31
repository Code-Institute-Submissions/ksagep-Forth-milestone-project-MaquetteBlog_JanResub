"""List of parts of comment form"""
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        """Determine the type of fields of comment"""
        model = Comment
        fields = ('body',)
