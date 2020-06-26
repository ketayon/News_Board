from django import forms
from .models import Message, Comment

class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'