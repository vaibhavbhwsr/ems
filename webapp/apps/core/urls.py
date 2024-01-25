from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import MyLoginView, MySignupView, MyLogoutView, HomePage, UpdateProfileView

app_name = "core"

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="core:login", permanent=False), name="index"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("signup/", MySignupView.as_view(), name="signup"),
    path("accounts/logout/", MyLogoutView.as_view(), name="logout"),
    # Password Reset
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="core/pass/password_reset_form.html",
            email_template_name="core/pass/password_reset_email.html",
            subject_template_name="core/pass/password_reset_subject.txt",
            success_url=reverse_lazy("core:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="core/pass/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="core/pass/password_reset_confirm.html",
            success_url=reverse_lazy("core:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="core/pass/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    path("home/", HomePage.as_view(), name="home"),
    path("update-profile/", UpdateProfileView.as_view(), name="update_profile"),
    # Password change
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="core/pass_2/password_change_form.html",
            success_url=reverse_lazy("core:password_change_done")
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="core/pass_2/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
