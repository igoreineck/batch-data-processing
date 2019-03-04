from __future__ import division

import os
import shutil
import time


class DataGenerate:

    def __init__(self, request, path):
        self.__request = request
        self.__path = path
        self.__data = []

    def clean_data_directory(self):
        shutil.rmtree(self.__path)
        os.mkdir(self.__path)

    def get_data(self):
        for item in self.__request['matches']:
            string =\
            """Game date: {gameDate} | {homeTeam} [{homeGoals}] x [{awayGoals}] {awayTeam}\n""".format(
                homeTeam=item['homeTeam']['name'],
                awayTeam=item['awayTeam']['name'],
                homeGoals=item['score']['fullTime']['homeTeam'],
                awayGoals=item['score']['fullTime']['awayTeam'],
                gameDate=item['utcDate'],
            )
            self.__data.append(string)

    def save_to_files(self):
        self.clean_data_directory()

        self.batchs = int(input('How many items do you want to see in the page?: '))
        qty_files = int(len(self.__data)/self.batchs)

        start_time = time.time()

        counter = 0
        with open(self.__path + 'results_0.txt', 'a') as file:
            for index, item in enumerate(self.__data):
                if counter == self.batchs:
                    file.close()
                    counter = 0
                    
                    LOCAL_PATH = f'{self.__path}result_{index}.txt'

                    file = open(LOCAL_PATH, 'a')

                file.write(item)
                counter += 1
            file.close()

        end_time = time.time()

        print("Proccess finished with success!")
        print("Duration: {total} seconds".format(total=end_time-start_time))

    """
    Think the better way to show a simple block of information based on batch inserted
    """
    def read_files(self):
        for item in os.listdir(self.__path):
            with open(self.__path + item, 'r') as file:
                file_content = file.readlines()
            file.close()
