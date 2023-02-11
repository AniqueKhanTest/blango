from blango_auth import views
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
urlpatterns = [

    path("accounts/profile/", views.profile, name='profile'),
    path("accounts/register/",
         RegistrationView.as_view(form_class=BlangoRegistrationForm), name='django_registration_register'),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
