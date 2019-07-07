from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name',)

        # For password is write only
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        """
        Create User
        """

        user_obj = User.objects.create(**validated_data)
        user_obj.set_password(validated_data['password'])
        user_obj.save()
        return user_obj