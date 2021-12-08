from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field to test our APIView"""
    name = serializers.CharField(max_length=10)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
