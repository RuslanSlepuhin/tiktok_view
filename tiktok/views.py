from rest_framework import permissions, generics
from rest_framework.response import Response

from .serializers import AuthSerializer, CallBackSerializer

class AuthViews(generics.GenericAPIView):
    serializer_class =AuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"data": serializer.data})

class CallBackViews(generics.GenericAPIView):
    serializer_class = CallBackSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"data": serializer.data})


