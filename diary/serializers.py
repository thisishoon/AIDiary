from diary.models import Diary
from django.contrib.auth.models import User
from rest_framework import serializers

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'