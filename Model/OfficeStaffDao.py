import logging
import sqlite3

from Model.DB_connection import DB_connection

logging.basicConfig(filename='../logging.log', filemode='w', format='%(asctime)s - %(levelname)s -%(message)s',
                    level=logging.INFO)


class OfficeStaffDao(DB_connection):

    def __init__(self):

        super().__init__()

    """The class is used to all backed activities that are made by office staff object."""

    """When we want  to remove the car in database, the caller can be pass the car's registration-
    number to this method. finally the car would be removed from the car table."""

    # carRegNo :- car's registration number.
    def remove_car(self, carRegNo):
        try:
            connect = self.get_connection()
            connect.execute('PRAGMA foreign_keys = on')
            cursor = connect.cursor()
            logging.info('Connect the database successfully for remove the car from table')

            # Deleting car record now
            sql_delete_query = """DELETE from car where reg_no = ?"""
            cursor.execute(sql_delete_query, (carRegNo,))
            connect.commit()
            logging.info('Car deleted successfully')
            cursor.close()
            return True

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while delete car', error)
            return False

        finally:
            self.close_connection(connect)

    def carData(self, modelName=None, manufactureName=None):
        """The car data  get from database will be change according the argument type.
        get the data from model the result list under the given model. it same as-
         manufacture name. maybe the result will be both modelName and manufacture-
         name. due to that reason method overloading is used to implement this function."""
        record = None
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch the car information.')

            if modelName is not None and manufactureName is None:
                # The fetch result under the model name.
                query = "select * from car where model_id in (select model_id from model where model_name = ?)"
                cursor.execute(query, (modelName,))
                record = cursor.fetchall()

            elif modelName is None and manufactureName is not None:
                # The fetch result under the manufacture name.
                query = "SELECT * from car WHERE model_id in (SELECT model_id FROM model WHERE manufacture_id in (SELECT manufacture_id from manufacture WHERE manufacture_name = ?))"
                cursor.execute(query, (manufactureName,))
                record = cursor.fetchall()

            else:
                # The fetch result under the both manufacture and model name.
                query = "SELECT * from car where model_id in (SELECT model_id from model WHERE model_name = ?) OR model_id in (SELECT model_id from model WHERE manufacture_id in (SELECT manufacture_id FROM manufacture WHERE manufacture_name = ?))"
                cursor.execute(query, (modelName, manufactureName,))
                record = cursor.fetchall()

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while getting data', error)
            return False
            # print(False)

        else:
            cursor.close()
            return record
            # print(record)

        finally:
            self.close_connection(connect)

    # Create method for sold car final price
    def fetchSoldCarFinalAmount(self, regNo):
        """Get the specify sold car car final amount"""
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch the final amount')

            query = 'SELECT sale.final_amount from sale WHERE reg_no = ?'
            cursor.execute(query,(regNo,))
            finalAmount = cursor.fetchall()
            cursor.close()
            logging.info('Successfully fetched the final amount from sale table.')
            return  finalAmount[0][0]

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while getting data', error)
            return False

        finally:
            self.close_connection(connect)

# OfficeStaffDao().carData(manufactureName='Dart', modelName='NG')


