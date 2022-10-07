from rest_framework import serializers
from api.models import Questions,Answers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name',]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    created_date = serializers.CharField(read_only=True)
    class Meta:
        model=Questions
        fields="__all__"

class AnswerSeriallizer(serializers.ModelSerializer):
    questions=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    upvote=serializers.CharField(required=True)
    posted_date=serializers.CharField(read_only=True)
    class Meta:
        model=Answers
        fields="__all__"