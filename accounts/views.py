from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class ChangePasswordView(CreateView):
    template_name = 'registration/password_change_form.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('password_change_done')

class ChangePasswordDoneView(CreateView):
    template_name = 'registration/password_change_done.html'
