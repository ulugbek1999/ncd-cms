"""ncd_static_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from vacancy.urls import urlpatterns as vacancy_urls

handler404 = 'ncd_cms.views.handler404'
handler500 = 'ncd_cms.views.handler500'

urlpatterns = [
    path('', include('ncd_cms.urls')),
    path('about/', include('about.urls')),
    path('service/', include('service.urls')),
    path('partner/', include('partner.urls')),
    path('feedback/', include('feedback.urls')),
    path('employee/', include('employee.urls')),
    path('document/', include('document.urls')),
    path('slider/', include('slider.urls')),
    path('faq/', include('faq.urls')),
    path('extra/', include('extra.urls')),
    path('edu/', include('edu.urls')),
    path('ads/', include('ads.urls')),
    path('api/', include('api.urls')),
    path('vacancy/', include(vacancy_urls)),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
