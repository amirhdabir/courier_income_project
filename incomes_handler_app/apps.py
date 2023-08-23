from django.apps import AppConfig


class IncomesHandlerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'incomes_handler_app'

    def ready(self):
        import incomes_handler_app.signals
