from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.response import Response

from .serializers import AuthSerializer, CallBackSerializer

class AuthViews(generics.GenericAPIView):
    serializer_class =AuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        print(request.data)
        # return render(request, request)
        return Response({"data": serializer.data})

    # def get(self, request):
    #     return

class CallBackViews(generics.GenericAPIView):
    serializer_class = CallBackSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"data": serializer.data})

class LinkedInCallBackView(generics.GenericAPIView):

    def post(self, request):
        return Response({"data": request.data})


