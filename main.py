from sender import sender
from verifier import verifier
import json


def main(event, context):
    request_strings = event['body'].split('&')
    request = {}
    for request_string in request_strings:
        key, value = request_string.split('=')
        request[key] = value

    if ('page' not in request) or (request['page'] not in ['HawkEvents']):
        return response_error(400, "Unknown Page")

    if 'g-recaptcha-response' not in request:
        return response_error(400, "Google Recaptcha Response Not Found")

    verify_result = verifier(request['page'], request['g-recaptcha-response'])

    return {
        "statusCode": 200,
        "body": json.dumps(verify_result)
    }

    status, msg = sender("i@iltc.io", "i@iltc.io", "Test Email", "This is our second email. We use it to test the function~")

    if status:
        response = {
            "statusCode": 200,
            "body": "OK"
        }
        return response
    else:
        response = {
            "statusCode": 500,
            "body": msg
        }
        return response


def response_error(status_code, body):
    return {
        "statusCode": status_code,
        "body": body
    }