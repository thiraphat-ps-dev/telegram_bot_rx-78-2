from apscheduler.schedulers.blocking import BlockingScheduler
from telegram_bot import telegram_bot
import time
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=0, seconds=30)
def timed_job():
    telegram_bot()


sched.start()