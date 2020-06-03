from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""

        an_apiview = [
            'uses HTTP methods as function (get,post,patch,put,delete)',
            'is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Its mapped manually to URLs',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello -{name}'
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method': 'put'})

    def patch(self,request,pk=None):
        """handle  partial update an object"""
        return Response({'method': 'patch'})

    def delete(self,request,pk=None):
        """handle deleting an object"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset =[
            'user actions list create retrive update partial_update',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'hello', 'a_viewset':a_viewset})

    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """handle getting an objects by its Id"""
        return Response({'http_method': 'GET'})

    def update(self,request,pk=None):
        """handle updating an objects by its Id"""
        return Response({'http_method': 'PUT'})

    def partial_update(self,request,pk=None):
        """handle partial_update an objects by its Id"""
        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):
        """handle getting an objects by its Id"""
        return Response({'http_method': 'DELETE'})
