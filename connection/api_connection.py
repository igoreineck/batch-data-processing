import http.client
import json


"""
API for footbal result games: api.football-data.org
"""
class ApiConnection:
    __url = 'api.football-data.org'

    def __init__(self, token):
        self.__token = token
        self.connection = None

    def __create_connection(self):
        connection = http.client.HTTPConnection(self.__url)
        return connection

    def make_request(self, matches_path, date_parameters={}, method='GET'):
        headers = {
            'X-Auth-Token': self.__token,
        }

        self.connection = self.__create_connection()

        if date_parameters is not None:
            matches_path += '?'

            for key, value in date_parameters.items():
                matches_path += f'{key}={value}'
                matches_path += '&'

        self.connection.request(
            method,
            matches_path,
            None,
            headers
        )

        return json.loads(self.connection.getresponse().read().decode())