import http.client
import json


# Limite de dias anteriores ao atual = 10
def main():
    API_TOKEN = '1fe37e79eacd4a62821526080700271f'

    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': API_TOKEN }

    connection.request(
       'GET',
       '/v2/matches?dateFrom=2019-02-24&dateTo=2019-03-03',
       None, 
       headers
    )

    content = json.loads(connection.getresponse().read().decode())
    
    with open('test.txt', 'a') as file:
        for item in content['matches']:
            string =\
            """Game date: {gameDate} | {homeTeam} [{homeGoals}] x [{awayGoals}] {awayTeam}\n\n""".format(
                homeTeam=item['homeTeam']['name'],
                awayTeam=item['awayTeam']['name'],
                homeGoals=item['score']['fullTime']['homeTeam'],
                awayGoals=item['score']['fullTime']['awayTeam'],
                gameDate=item['utcDate'],
            )

            file.write(string)
    file.close()


if __name__ == '__main__':
    main()