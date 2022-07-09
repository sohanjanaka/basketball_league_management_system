from  rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.User
        field = ('id', 'email', 'name', 'password')
        extra_kargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """create and return a new user"""

        user = models.User(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        return user

