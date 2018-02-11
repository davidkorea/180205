from django import forms
from django.core.exceptions import ValidationError

def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('Not Enough Letters')

def comment_validator(comment):
    if 'a' in comment:
        raise ValidationError('Do Not Use the Word!')

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required': 'why no words?'
        },
        validators=[words_validator, comment_validator]
                              )