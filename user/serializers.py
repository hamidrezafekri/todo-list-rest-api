from rest_framework import serializers

from user.models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        password = validated_data['password']
        if not password:
            raise ValueError('password is required')
        else:
            instance.set_password(password)
        instance.save()
        return instance
