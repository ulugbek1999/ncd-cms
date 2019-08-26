from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from about.models import About
from .serializers import AboutSerializer


class AboutCreate(CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutUpdate(UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    lookup_url_kwarg = 'id'


class AboutDelete(DestroyAPIView):
    queryset = About.objects.all()
    lookup_url_kwarg = 'id'
