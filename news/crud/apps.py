from django.apps import AppConfig


class CrudConfig(AppConfig):
    name = "crud"

    def ready(self):
        print("Starting scheduler...")
        from . import clock
        clock.start()

