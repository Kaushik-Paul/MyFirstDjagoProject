# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a API View features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, delete)',
            'Is similer to a traditional Django View',
            'Gives you the most over the applicaion logic',
            'Is mapped manually to the URLs'
        ]
        return Response({'message': 'Hello World', 'an_apiview': an_apiview})
