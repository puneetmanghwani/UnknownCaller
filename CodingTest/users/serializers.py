from rest_framework import serializers
from users.models import CustomUser
from rest_auth.registration.serializers import RegisterSerializer

# Custom User Serializer extending registration functionality of all-auth registration to validate phone number and store data in model.
class UserSerializer(RegisterSerializer):
    full_name = serializers.CharField(required=True)
    phone_no = serializers.CharField(required=True)

    def validate_phone_no(self, value):
        if CustomUser.objects.filter(phone_no=value).exists():
            raise serializers.ValidationError("Phone Numbe already exist")
        return value
    def custom_signup(self, request, user):
        user.full_name = self.validated_data.get('full_name')
        user.phone_no = self.validated_data.get('phone_no')
        user.save(update_fields=['full_name','phone_no'])

