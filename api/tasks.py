from celery import Celery
from .services import TextSender

app = Celery(
    'tasks',
    broker='redis://localhost:6379/',
)


@app.task(bind=True, queue='send')
def send_text(self, email, phone_number, text):
    print('send email celery task ........')
    print('send sms celery task ........')

    try:
        text_sender = TextSender()
        text_sender.send(email=email, phone_number=phone_number, text=text)
    except Exception as exc:
        print(f'------------ exc: {exc}')
        raise self.retry(exc=exc)

    print('finished sending email .....')
    print('finished sending sms .....')

