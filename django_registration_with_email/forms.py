from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django_registration.forms import RegistrationFormUniqueEmail

User = get_user_model()

User.USERNAME_FIELD = 'email'
User.REQUIRED_FIELDS = ['username']


def get_user_by_email(email):
    try:
        user = User.objects.filter(email__iexact=email, is_active=True).get()
    except User.MultipleObjectsReturned:
        user = User.objects.filter(email__exact=email, is_active=True).get()
    except User.DoesNotExist:
        try:
            user = User.objects.filter(email__iexact=email).get()
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email__exact=email).get()
        except User.DoesNotExist:
            try:
                user = User.objects.filter(username__exact=email, is_active=True).get()
            except User.DoesNotExist:
                user = User.objects.filter(username__exact=email).get()
    return user


class REPasswordResetForm(PasswordResetForm):
    captcha = CaptchaField()

    def clean_email(self):
        """
        Validate that the email is not already in use.
        """
        email = self.cleaned_data['email']
        user = get_user_by_email(email)
        if user:
            if not user.is_active:
                raise forms.ValidationError(
                    format_html(
                        _("User with this e-mail is not active. Please {} your account first."),
                        format_html(
                            "<a href='{activate_url}'>{activate_text}</a>",
                            activate_url=reverse('registration_resend_activation'),
                            activate_text=_("activate"),
                        ),
                    ),
                )

            # Generate random password, so that the e-mail is sent
            if not user.has_usable_password():
                user.password = User.objects.make_random_password()
                user.save()
        else:
            raise forms.ValidationError(
                "We don't have this e-mail in our system. Please check if you registered with this e-mail",
            )

        return email


class LoginForm(AuthenticationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        user = get_user_by_email(username)
        if not user:
            return username
        if not user.is_active:
            raise forms.ValidationError(
                format_html(
                    _("This account has not been activated yet. {}."),
                    format_html(
                        "<a href='{activate_url}'>{activate_text}</a>",
                        activate_url=reverse('registration_resend_activation'),
                        activate_text=_("Resend activation mail"),
                    ),
                ),
            )
        return user.email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username or e-mail"


class FullUserRegistrationForm(RegistrationFormUniqueEmail):
    class Meta(RegistrationFormUniqueEmail.Meta):
        model = User
        fields = [
            'email',
            'password1',
            'password2',
        ]
