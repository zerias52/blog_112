from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("changepass/", PasswordChangeView.as_view(), name="changepass"),
]