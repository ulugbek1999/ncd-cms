from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from faq.models import Faq, FaqCategory
from .serializers import FaqSerializer, FaqCategorySerializer


class FaqCreate(CreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqUpdate(UpdateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    lookup_url_kwarg = 'id'


class FaqDelete(DestroyAPIView):
    queryset = Faq.objects.all()
    lookup_url_kwarg = 'id'


class FaqCategoryCreate(CreateAPIView):
    queryset = FaqCategory.objects.all()
    serializer_class = FaqCategorySerializer


class FaqCategoryUpdate(UpdateAPIView):
    queryset = FaqCategory.objects.all()
    serializer_class = FaqCategorySerializer
    lookup_url_kwarg = 'id'


class FaqCategoryDelete(DestroyAPIView):
    queryset = FaqCategory.objects.all()
    lookup_url_kwarg = 'id'
