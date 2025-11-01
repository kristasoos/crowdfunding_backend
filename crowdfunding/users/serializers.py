from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields='__all__'
        # for the PW not be able to be read nor called back
        # This is a security feature to prevent the password from being exposed in API responses.
  
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            return CustomUser.objects.create_user(**validated_data)

        # def create(self, validated_data):
        #     user = CustomUser(
        #         email=validated_data['email'],
        #         username=validated_data['username']
        #     )
        #     user.set_password(validated_data['password'])
        #     user.save()
        #     return user



    