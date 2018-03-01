from sender import sender
from verifier import verifier
import json
import urllib


def main(event, context):
    request = urllib.parse.parse_qs(event['body'])

    form_items = [['name', 'your name'],
                  ['email', 'the e-mail address'],
                  ['subject', 'the subject'],
                  ['message', 'the message']]

    for item in form_items:
        if item[0] not in request:
            return response_error(400, "Please fill " + item[1])

    if ('page' not in request) or (request['page'][0] not in ['HawkEvents']):
        return response_error(400, "Unknown Page")

    if 'g-recaptcha-response' not in request:
        return response_error(400, "Google reCAPTCHA Response Not Found")

    verify_result = verifier(request['page'][0], request['g-recaptcha-response'][0])

    if not verify_result['success']:
        return response_error(403, "Google reCAPTCHA Failed")

    to_emails = {'HawkEvents': 'hawkevents@outlook.com'}


    status, msg = sender(
        request['email'][0],
        to_emails[request['page'][0]],
        '[{} - {}] '.format(request['page'][0], request['name'][0]) + request['subject'][0],
        request['message'][0])

    if status:
        return {
            "statusCode": 200,
            "body": "Thank you!"
        }
    else:
        return response_error(500, "We cannot send the email: " + msg)


def response_error(status_code, body):
    return {
        "statusCode": status_code,
        "body": body
    }
