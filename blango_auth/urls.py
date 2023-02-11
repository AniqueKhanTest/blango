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
    path("accounts/", include("allauth.urls")),


]


# client id --> 596069966448-albmeb7rb7i7l4tl9447inavqhafocnu.apps.googleusercontent.com
# secret key  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
