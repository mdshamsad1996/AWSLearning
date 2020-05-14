"""Http response based on headers_value"""
import requests


class HttpResponse():
    """HttpResponse by provideing headers_value"""

    def get_http_reponse(self, headers_value=None):
        """Method for provide response object"""

        response = requests.get(
            'https://ugmvjtpg4d.execute-api.us-east-1.amazonaws.com/Stage/',
            headers={'Authorization': headers_value}
            )
        return response
