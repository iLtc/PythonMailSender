from sender import sender


def main(event, context):
    request_strings = event['body'].split('&')
    request = {}
    for request_string in request_strings:
        key, value = request_string.split('=')
        request[key] = value

    status, msg = sender("i@iltc.io", "i@iltc.io", "Test Email", "This is our second email. We use it to test the function~")

    if status:
        response = {
            "statusCode": 200,
            "body": "OK"
        };
        return response
    else:
        response = {
            "statusCode": 500,
            "body": msg
        };
        return response
