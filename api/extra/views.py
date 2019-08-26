from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from extra.models import Extra
from .serializers import ExtraSerializer


class ExtraCreate(CreateAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class ExtraUpdate(UpdateAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
    lookup_url_kwarg = 'id'


class ExtraDelete(DestroyAPIView):
    queryset = Extra.objects.all()
    lookup_url_kwarg = 'id'
