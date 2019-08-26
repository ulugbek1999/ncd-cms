from rest_framework.generics import UpdateAPIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserUpdate(UpdateAPIView):
    """
    change username and password
    """
    serializer_class = UserSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data.get("username"))
            if serializer.data.get("username"):
                self.object.username = serializer.data.get("username")
                self.object.save()
            print(serializer.data.get("new_password"))
            if serializer.data.get("new_password") and serializer.data.get("new_password") != "":
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong"]}, status=status.HTTP_400_BAD_REQUEST)

                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
            return Response("Success", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
