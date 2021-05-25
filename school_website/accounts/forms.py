from django.contrib.auth.forms import AuthenticationForm

class AuthenticationFormCustom(AuthenticationForm):
    error_messages = {
        'invalid_login': "Invalid password or username",
        'inactive': "This account is inactive.",
    }
