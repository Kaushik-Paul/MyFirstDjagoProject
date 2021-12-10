# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a API View features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most over the application logic',
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


class HelloViewSet(ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello World Message"""
        an_apiview = [
            'Uses Action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': "Hello How Are You????", 'an_apiview': an_apiview})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!!!!"

            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, format=None, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handling updating an object"""
        return Response({'http_method': "PUT"}, status=status.HTTP_202_ACCEPTED)

    def partial_update(self, request, pk=None):
        """Handling partial update of an object"""
        return Response({'http_method': 'PATCH'}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        """Handling removing an object"""
        return Response({'http_method': 'DELETE'})
