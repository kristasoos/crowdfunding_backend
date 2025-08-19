from rest_framework import serializers
from .models import CustomUser

class CustomserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields='__all__'
        # for the PW not be able to be read nor called back
        # This is a security feature to prevent the password from being exposed in API responses.
  
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def creat(self, validated_data):
            return CustomUser.objects.create_user(**validated_data)