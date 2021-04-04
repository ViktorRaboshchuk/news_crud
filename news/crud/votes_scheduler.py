"""Advanced Python Scheduler (APScheduler) is
a Python library that lets you schedule your code to be executed later,
either just once or periodically. """
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    """Schedules a job foe deleting all upvotes from views.py once a day"""
    scheduler = BackgroundScheduler()
    from crud.views import VotesDeleteView

    vote_up = VotesDeleteView()
    scheduler.add_job(
        vote_up.delete,
        "interval",
        days=1,
        id="delete_votes_001",
        replace_existing=True,
    )
    scheduler.start()
