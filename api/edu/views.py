from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from edu.models import Edu, Document
from .serializers import EduSerializer
from rest_framework.response import Response


class EduCreate(CreateAPIView):
    serializer_class = EduSerializer

    def get_queryset(self, request):
        return Edu.objects.all()


class EduUpdate(UpdateAPIView):
    queryset = Edu.objects.all()
    serializer_class = EduSerializer
    lookup_url_kwarg = 'id'


class EduDelete(DestroyAPIView):
    queryset = Edu.objects.all()
    lookup_url_kwarg = 'id'


class DocumentDelete(DestroyAPIView):
    queryset = Document.objects.all()
    lookup_url_kwarg = 'id'
