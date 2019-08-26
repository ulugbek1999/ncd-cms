from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from feedback.models import Feedback
from .serializers import FeedbackSerializer


class FeedbackCreate(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackUpdate(UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_url_kwarg = 'id'


class FeedbackDelete(DestroyAPIView):
    queryset = Feedback.objects.all()
    lookup_url_kwarg = 'id'
