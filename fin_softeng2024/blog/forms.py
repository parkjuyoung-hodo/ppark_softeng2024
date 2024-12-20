from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',  # Bootstrap 스타일 적용
                'rows': 3,  # 텍스트 입력창 높이
                'placeholder': 'Write your comment!',  # 입력 안내
            }),
        }