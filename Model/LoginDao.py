import logging
import sqlite3

from Model.DB_connection import DB_connection

logging.basicConfig(filename='../logging.log', filemode='w', format='%(asctime)s - %(levelname)s -%(message)s',
                    level=logging.INFO)


class LoginDAO(DB_connection):

    """The backend for user validation, It returns to caller the all user information that are store in-
    user table. """

    def getUserInfo(self):
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully to fetch the user information')

            # Query for fetch the user information from user table
            query = 'select * from user'
            cursor.execute(query)
            records = cursor.fetchall()
            logging.info('Successfully fetched the data from user table')
            cursor.close()
            return records

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while getting data from user table', error)

        finally:
            self.close_connection(connect)
