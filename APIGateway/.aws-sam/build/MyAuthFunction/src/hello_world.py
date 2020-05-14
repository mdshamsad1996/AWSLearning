""""lambda handler for Hello WOrld"""


def handler(event, context):
    """Handler function"""

    return {'body': 'Hello World!', 'statusCode': 200}
