"""apps describes a Python package that provides some set of features"""
from django.apps import AppConfig


class CrudConfig(AppConfig):
    name = "crud"

    def ready(self):
        """ready func perform initialization tasks"""
        print("Starting scheduler...")
        from crud import votes_scheduler

        votes_scheduler.start()
