from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'uses HTTP methods as function (get,post,patch,put,delete)',
            'is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Its mapped manually to URLs',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
