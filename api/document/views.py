from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from document.models import Document
from .serializers import DocumentSerializer


class DocumentCreate(CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentUpdate(UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_url_kwarg = 'id'


class DocumentDelete(DestroyAPIView):
    queryset = Document.objects.all()
    lookup_url_kwarg = 'id'
