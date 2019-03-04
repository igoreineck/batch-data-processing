if __name__ == '__main__':
    import os

    from connection.api_connection import ApiConnection
    from connection.data_generate import DataGenerate


    connection = ApiConnection('1fe37e79eacd4a62821526080700271f')
    PROJECT_PATH = os.getcwd() + '/data/'

    parameters = {
        'dateFrom': '2019-02-24',
        'dateTo': '2019-03-03'
    }

    request = connection.make_request(
        '/v2/matches',
        parameters
    )

    process = DataGenerate(request, PROJECT_PATH)
    process.get_data()
    process.save_to_files()