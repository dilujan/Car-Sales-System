import sqlite3
import logging

logging.basicConfig(filename='../logging.log', filemode='w', format='%(asctime)s - %(levelname)s -%(message)s',
                    level=logging.INFO)


class DB_connection:

    def __init__(self):
        self.__connection = None

        # Connect the database

    def get_connection(self):
        self.__connection = sqlite3.connect('../rush_carSales.db')
        return self.__connection

        # Close the connection

    def close_connection(self, connect):
        if connect:
            connect.close()
            logging.info('Close the database successfully')
