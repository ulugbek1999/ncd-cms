from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class LoginPageView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=username, password=pwd)
        if user:
            login(request, user)
            # if request.GET.get('next'):
            #     return HttpResponseRedirect(request.GET.get('next'))
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('index'))
        return render(request, 'auth/login.html', {'error': True})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
