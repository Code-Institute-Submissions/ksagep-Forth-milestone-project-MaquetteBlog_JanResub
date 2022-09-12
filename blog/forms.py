from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        modell = Comment
        fields = ('body',)
        