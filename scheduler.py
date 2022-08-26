from ast import arg
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from ocr import make_pred

sched  = BackgroundScheduler()

def set_schedule():
    # sched  = BackgroundScheduler()
    url = "https://fileuploadapp.blob.core.windows.net/tutorial-container/sdfadfas.png"
    sched.add_job(make_pred,"cron",args=[url]),
    # make_pred()
    sched.start()
    sched.print_jobs()
    return "okay"
print(set_schedule())
print(sched.print_jobs())