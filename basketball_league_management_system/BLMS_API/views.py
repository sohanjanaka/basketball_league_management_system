from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


class HelloApiView(APIView):
    """Hello world API"""

    def get(self, request, format=None):

        an_apiview = [
            'just a list',
            'of API view',
            'keep adding',
            'things'
        ]

        return Response({'msg': 'hello world', 'test': an_apiview})


class HelloViewSet(viewsets.ViewSet):
    """Hello viewset"""

    @classmethod
    def get_extra_actions(cls):
        return []

    def list(self, request):
        a_viewset = [
            "viewset",
            "helloworld"
        ]

        return Response({
            "message": "Hellow viewset",
            "list": a_viewset
        })
