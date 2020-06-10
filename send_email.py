import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email_with_text(text, email_from, email_to):
    message = Mail(
        from_email='ilkaeva85@rambler.ru',
        to_emails='ilkaevagulchachak85@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content=f'<strong>{text}</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return response
    except Exception as e:
        print(e.body)