from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()

scheduler.add_job(lambda: scheduler.print_jobs(), 'interval', seconds=5)

scheduler.start()
