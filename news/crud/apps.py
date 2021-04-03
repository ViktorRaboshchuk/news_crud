from django.apps import AppConfig


class CrudConfig(AppConfig):
    name = "crud"

    def ready(self):
        print("Starting scheduler...")
        from .scheduler import votes_scheduler
        votes_scheduler.start()

