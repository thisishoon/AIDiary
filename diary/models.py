from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("내용", blank=True, null=True)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("변경 시간", auto_now=True)
    happiness = models.IntegerField("행복", null=True, blank=True, default=None)
    neutrality = models.IntegerField("중립", null=True, blank=True, default=None)
    sadness = models.IntegerField("슬픔", null=True, blank=True, default=None)
    worry = models.IntegerField("걱정", null=True, blank=True, default=None)
    anger = models.IntegerField("분노", null=True, blank=True, default=None)
    qna = models.TextField("질문", null=True, blank=True, default=None)


    class Meta:
        ordering = ['-created_at'];

