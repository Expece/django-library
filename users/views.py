from django.views.generic import UpdateView, CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .forms import SignUpUserForm, SignInUserForm, UserEditForm
from .utils import DataMixin


class UserProfile(ListView):
    model = User
    template_name = 'users/profile.html'
    slug_url_kwarg = 'user_slug'

class UpdateUser(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/userupdate.html'

class SignUpUser(DataMixin, CreateView):
    form_class = SignUpUserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('signin')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('library')


class SignInUser(DataMixin, LoginView):
    form_class = SignInUserForm
    template_name = 'users/signin.html'
    def get_success_url(self):
        return reverse_lazy('library')


def signOutUser(request):
    logout(request)
    return redirect('library')
