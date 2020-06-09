from rest_framework import serializers
from users.models import CustomUser
from rest_auth.registration.serializers import RegisterSerializer

class SearchSerializer(serializers.Serializer):
    id=serializers.IntegerField(required=True)
    full_name = serializers.CharField(required=True)
    phone_no = serializers.CharField(required=True)
    spam_count=serializers.IntegerField(required=True)

class DetailSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=True)
    phone_no = serializers.CharField(required=True)
    spam_count=serializers.IntegerField(required=True)
    email= serializers.CharField(required=False)