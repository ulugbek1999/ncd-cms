from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from ads.models import AdsBlock, AdsBlockImage
from .serializers import AdsBlockSerializer


class AdsCreate(CreateAPIView):
    queryset = AdsBlock.objects.all()
    serializer_class = AdsBlockSerializer


class AdsUpdate(UpdateAPIView):
    queryset = AdsBlock.objects.all()
    serializer_class = AdsBlockSerializer
    lookup_url_kwarg = 'id'


class AdsDelete(DestroyAPIView):
    queryset = AdsBlock.objects.all()
    lookup_url_kwarg = 'id'


class AdsImageDelete(DestroyAPIView):
    queryset = AdsBlockImage.objects.all()
    lookup_url_kwarg = 'id'
