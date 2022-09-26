from rest_framework import serializers

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {'write_only': True},
            'is_active': {'write_only': True},
            'is_admin': {'write_only': True},
        }













# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer(required=True)
#     class Meta:
#         model = User
#         fields = ('phone_number', 'email', 'full_name', 'is_active', 'is_admin')

#     def create(self, validated_data):

#         # create user 
#         user = User.objects.create(
#             phone_number = validated_data['phone_number'],
#             email = validated_data['email'],
#             # etc ...
#         )

#         profile_data = validated_data.pop('profile')
#         # create profile
#         profile = Profile.objects.create(
#             user = user
#             first_name = profile_data['first_name'],
#             last_name = profile_data['last_name'],
#             # etc...
#         )

#         return user










