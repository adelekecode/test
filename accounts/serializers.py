from rest_framework import serializers

class LogoutSerializers(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=350)


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=350)
    password = serializers.CharField(max_length=350)


