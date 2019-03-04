import os

from os.path import join, dirname
from dotenv import load_dotenv
 

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


if __name__ == '__main__':
    from connection.api_connection import ApiConnection
    from connection.data_generate import DataGenerate

    SECRET_KEY = os.getenv('API_TOKEN')

    connection = ApiConnection(SECRET_KEY)
    PROJECT_PATH = os.getcwd() + '/data/'

    parameters = {
        'dateFrom': '2019-02-24',
        'dateTo': '2019-03-03'
    }

    request = connection.make_request(
        '/v2/matches',
        parameters
    )

    proccess = DataGenerate(request, PROJECT_PATH)
    proccess.get_data()
    proccess.save_to_files()
    proccess.read_files()