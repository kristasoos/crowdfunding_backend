from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields='__all__'
        # for the PW not be able to be read nor called back
        # This is a security feature to prevent the password from being exposed in API responses.
  
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            password = validated_data.pop("password", None)
            user = CustomUser(**validated_data)
            if password:
                user.set_password(password)
            else:
                user.set_unusable_password()
            user.save()
            return user

        # def create(self, validated_data):
        #     user = CustomUser(
        #         email=validated_data['email'],
        #         username=validated_data['username']
        #     )
        #     user.set_password(validated_data['password'])
        #     user.save()
        #     return user



    