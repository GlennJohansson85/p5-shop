from django.apps import AppConfig


class AccountsConfig(AppConfig):
    '''
    Configuration class for the accounts app.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
