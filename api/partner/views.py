from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from partner.models import Partner
from .serializers import PartnerSerializer


class PartnerCreate(CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerUpdate(UpdateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_url_kwarg = 'id'


class PartnerDelete(DestroyAPIView):
    queryset = Partner.objects.all()
    lookup_url_kwarg = 'id'
