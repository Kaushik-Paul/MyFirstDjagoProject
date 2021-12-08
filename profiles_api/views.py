# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a API View features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, delete)',
            'Is similer to a traditional Django View',
            'Gives you the most over the applicaion logic',
            'Is mapped manually to the URLs'
        ]
        return Response({'message': 'Hello World', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, format=None, pk=None):
        """Handling updating an object"""
        return Response({'message': 'PUT Request'})

    def patch(self, request, format=None, pk=None):
        """Handling the partial update to an object"""
        return Response({'message': "PATCH Request"}, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None, pk=None):
        """Delete an object"""
        return Response({'message': "DELETE Request"}, status=status.HTTP_202_ACCEPTED)
