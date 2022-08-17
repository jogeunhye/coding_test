from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#게시판
class Board(models.Model):
    user = models.ForeignKey(User, verbose_name='이름', on_delete=models.SET_NULL, null=True)
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField(verbose_name='내용')

# 댓글
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='이름', on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name='내용')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

# 좋아요
class Like(models.Model):
    user = models.ForeignKey(User, verbose_name='이름', on_delete=models.SET_NULL, null=True)
    like = models.BooleanField(verbose_name='좋아요여부', default=False)
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)