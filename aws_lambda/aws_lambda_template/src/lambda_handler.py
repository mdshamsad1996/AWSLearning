'''
    Lambda handler  Module for  request library implementation
'''
import requests
from requests.exceptions import HTTPError


def lambda_handler(event=None, context=None):                                                         # pylint: disable=C0303,W0613
    '''
    Lambda_handler function for aws lambda handler
    '''
    url = "https://github.com/anidok/python-unittest-classroom"

    return get_response(url)


def get_response(url):
    '''
    Get response  using given url
    '''
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:                                                                            # pylint: disable=W0703,C0303 
        return f'Other error occurred: {err}'
    else:
        return 'Success!'
