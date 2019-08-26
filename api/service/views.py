from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from service.models import Service
from .serializers import ServiceSerializer


class ServiceCreate(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdate(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_url_kwarg = 'id'


class ServiceDelete(DestroyAPIView):
    queryset = Service.objects.all()
    lookup_url_kwarg = 'id'
