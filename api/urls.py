from django.urls import path, include

urlpatterns = [
    path('about/', include('api.about.urls')),
    path('service/', include('api.service.urls')),
    path('partner/', include('api.partner.urls')),
    path('feedback/', include('api.feedback.urls')),
    path('employee/', include('api.employee.urls')),
    path('document/', include('api.document.urls')),
    path('faq/', include('api.faq.urls')),
    path('slider/', include('api.slider.urls')),
    path('extra/', include('api.extra.urls')),
    path('edu/', include('api.edu.urls')),
    path('profile/', include('api.profile.urls')),
    path('ads/', include('api.ads.urls')),
    path('vacancy/', include('api.vacancy.urls'))
]
