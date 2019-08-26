from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    password and username change serializer.
    """
    old_password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
