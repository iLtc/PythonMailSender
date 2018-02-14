from sender import sender

def main(event, context):
    sender("i@iltc.io", "i@iltc.io", "Test Email", "This is our second email. We use it to test the function~")

    response = {
        "statusCode": 200,
        "body": "OK"
    };
    return response
