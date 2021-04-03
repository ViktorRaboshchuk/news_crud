from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(print("BLAAAAAAAAAAAAAAAA"), 'interval', seconds=10)
    scheduler.start()
