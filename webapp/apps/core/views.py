from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import MyLoginForm, RegistrationForm

User = get_user_model()

# Create your views here.


class MySignupView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = "core/signup.html/"
    success_url = "/"
    success_message = (
        "%(username)s was created successfully! Now Login with"
        " the same username and password!"
    )

    def test_func(self):
        """
        This is necessary function to use with UserPassesTextMixin
        """
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        """
        This function stop accessing signup page to logged in user
        """
        return HttpResponseRedirect(reverse("users:home"))


class MyLoginView(SuccessMessageMixin, LoginView):
    """
    Here it stops logged in user to access log in page.
    And add success message
    """

    form_class = MyLoginForm
    template_name = "core/login.html"
    redirect_authenticated_user = True
    success_message = "%(username)s, Welcome Here!"


class MyLogoutView(LogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class HomePage(TemplateView):
    template_name = "core/user/home.html"


@method_decorator(login_required, name="dispatch")
class UpdateProfileView(UpdateView, SuccessMessageMixin):
    model = User
    template_name = "core/user/update_profile.html"
    fields = ["first_name", "last_name", "email", "phone", "address", "dp"]
    success_url = "/home/"
    success_message = "Your Profile Updated Successfully!"

    def get_object(self, **kwargs):
        return self.request.user
