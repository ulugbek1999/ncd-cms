from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Importing models
from slider.models import Slider
from about.models import About
from ads.models import AdsBlock
from document.models import Document
from edu.models import Edu
from employee.models import Employee
from extra.models import Extra
from faq.models import Faq
from feedback.models import Feedback
from partner.models import Partner
from service.models import Service
from vacancy.models import Vacancy
# Importing serializers
from api.slider.serializers import SliderSerializer
from api.about.serializers import AboutSerializer
from api.ads.serializers import AdsBlockSerializer
from api.document.serializers import DocumentSerializer
from api.edu.serializers import EduSerializer
from api.employee.serializers import EmployeeSerializer
from api.extra.serializers import ExtraSerializer
from api.faq.serializers import FaqSerializer
from api.feedback.serializers import FeedbackSerializer
from api.partner.serializers import PartnerSerializer
from api.service.serializers import ServiceSerializer
from api.vacancy.serializers import VacancySerializer


class CMSListView(APIView):
    '''CMSListView is requested by the '''
    '''client side that is running in Nuxt.js'''
    def get(self, request):
        # About
        about_model = About.objects.all()
        about_serializer = AboutSerializer(about_model, many=True)
        # Ads
        ads_model = AdsBlock.objects.all()
        ads_serializer = AdsBlockSerializer(ads_model, many=True)
        # Document
        doc_model = Document.objects.all()
        doc_serializer = DocumentSerializer(doc_model, many=True)
        # Slider
        sliders_model = Slider.objects.all()
        sliders_serializer = SliderSerializer(sliders_model, many=True)
        # Education
        edu_model = Edu.objects.all()
        edu_serializer = EduSerializer(edu_model, many=True)
        # Staff
        employee_model = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee_model, many=True)
        # Extra information
        extra_model = Extra.objects.all()
        extra_serializer = ExtraSerializer(extra_model, many=True)
        # Faq
        faq_model = Faq.objects.all()
        faq_serializer = FaqSerializer(faq_model, many=True)
        # Feedback
        feedback_model = Feedback.objects.all()
        feedback_serializer = FeedbackSerializer(feedback_model, many=True)
        # Partner
        partner_model = Partner.objects.all()
        partner_serializer = PartnerSerializer(partner_model, many=True)
        # Service
        service_model = Service.objects.all()
        service_serializer = ServiceSerializer(service_model, many=True)
        # Vacancy
        vacancy_model = Vacancy.objects.all()
        vacancy_serializer = VacancySerializer(vacancy_model, many=True)

        # The whole data to be returned as a response
        data = {
            "about": about_serializer.data,
            "ads": ads_serializer.data,
            "slider": sliders_serializer.data,
            "documents": doc_serializer.data,
            "education": edu_serializer.data,
            "employee": employee_serializer.data,
            "extra": extra_serializer.data,
            "faq": faq_serializer.data,
            "feedback": feedback_serializer.data,
            "partner": partner_serializer.data,
            "service": service_serializer.data,
            "vacancy": vacancy_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
