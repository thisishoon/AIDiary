from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("내용", blank=True, null=True)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("변경 시간", auto_now=True)
    feeling = models.IntegerField("감정도", null=True, blank=True, default=None)
    qna = models.TextField("질문?", null=True, blank=True, default=None)


    class Meta:
        ordering = ['-created_at'];

