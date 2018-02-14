from sender import sender

def main(event, context):
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
