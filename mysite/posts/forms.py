from django import forms
from .models import Post

# Takahashi Shunichi
class PostForm(forms.Form):
    content = forms.CharField(label='ポスト')
    title = forms.CharField(label='作品名')
    author = forms.CharField(label='著者名')


class CommentForm(forms.Form):
    """Form for comment on posts.

    Author:
        Masato Umakoshi
    """
    comment = forms.CharField(label='コメント')
