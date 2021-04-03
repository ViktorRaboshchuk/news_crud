from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=0.5)
def timed_job():
    print('This job is run every three minutes.')


# @scheduler.scheduled_job('cron', hour=24)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')


scheduler.start()