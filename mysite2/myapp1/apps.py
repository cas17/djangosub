from django.apps import AppConfig


class Myapp1Config(AppConfig):
    """
    Configuration class for the 'myapp1' Django app.

    This class defines the configuration for the 'myapp1' app. It specifies the
    default auto field for models and sets the name of the app.

    Attributes:
        default_auto_field (str): The default auto field to use for models.
            Set to 'django.db.models.BigAutoField' to use a big integer as the
            auto field for model primary keys.
        name (str): The name of the app. Should match the name used in the
            app's 'INSTALLED_APPS' configuration in Django settings.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp1'
