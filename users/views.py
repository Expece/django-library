from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import SignUpUserForm, SignInUserForm


class PersonalAccount(DetailView):
    template_name = 'users/personal_account.html'


class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('signin')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class SignIpUser(LoginView):
    form_class = SignInUserForm
    template_name = 'users/signin.html'

    def get_success_url(self):
        return reverse_lazy('home')


def signOutUser(request):
    logout(request)
    return redirect('home')
