from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from slider.models import Slider
from .serializers import SliderSerializer


class SliderCreate(CreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class SliderUpdate(UpdateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    lookup_url_kwarg = 'id'


class SliderDelete(DestroyAPIView):
    queryset = Slider.objects.all()
    lookup_url_kwarg = 'id'
