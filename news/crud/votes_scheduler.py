from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    from crud.views import VotesDeleteView
    vote_up = VotesDeleteView()
    scheduler.add_job(vote_up.delete, 'interval', seconds=20, id="delete_votes_001", replace_existing=True)
    scheduler.start()
