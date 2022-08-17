from django import forms
from django.contrib.auth.models import User
from .models import Board

class BoardForm(forms.ModelForm):

    class Meta :
        model = Board
        fields={'title', 'content'}
        label = {
            'title' : '제목', 
            'content': '내용'
           
        }
