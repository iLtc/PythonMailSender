import sendgrid
import os
from sendgrid.helpers.mail import *


def sender(from_email, to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(from_email)
    to_email = Email(to_email)
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        if response.status_code == 202:
            return True, ''
        else:
            return False, 'Unknown Error'

    except BaseException as e:
        return False, str(e)
