import threading
import time

from send_email import send_email_with_text

TASKS = []
NUMBER_OF_TASKS = 10 
EMAIL_FROM = 'ilkaeva85@rambler.ru'
EMAIL_TO = 'ilkaevagulchachak85@gmail.com'

def worker(text):
    send_email_with_text(text, EMAIL_FROM, EMAIL_TO)

def add_email_to_emails(text, timer):
    TASKS.append({"text": text, "timer": timer})
    t = threading.Timer(timer, worker, args=(text, ))
    t.start()

def get_last_tasks():
    return TASKS[-NUMBER_OF_TASKS:]
