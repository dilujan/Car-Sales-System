import logging
import sqlite3

from Model.DB_connection import DB_connection
from POJO.Car import Car
from POJO.CarModel import CarModel
from POJO.Manufacture import Manufacture

logging.basicConfig(filename='../logging.log', filemode='w', format='%(asctime)s - %(levelname)s -%(message)s',
                    level=logging.INFO)


class StaffDao(DB_connection):
    """A back end class for Staff, all the database operation that are made by Staff object,
     that happen here."""

    """It fetch the all manufacture details in manufacture table. add those information-
    into each manufacture object to hide the data (OOPs encapsulation). finally the collection-
     of manufacture objects add into a list. the list will be returns, when caller calls."""
    def fetchManufactureDetails(self):
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch the manufacture details in manufacture '
                         'manufacture table.')

            # Query for fetch the manufacture information from manufacture table
            query = 'SELECT * FROM manufacture'
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            logging.info('Successfully fetched the data from manufacture table.')

            # Create a empty manufacture list to collect the manufacture object.
            manufacture_list = []

            # fetch each row's record in records that fetch the data from manufacture-
            # table.
            for row in records:
                manufacture_id = row[0]
                manufacture_name = row[1]

                # Create an manufacture object and add values that are collected-
                # from in each row.
                manufacture = Manufacture(manufacture_id, manufacture_name)

                # The created manufacture object adds into list.
                manufacture_list.append(manufacture)

            logging.info("Successfully returns the manufacture list to caller.")
            return manufacture_list

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while getting data from manufacture table.', error)

        finally:
            self.close_connection(connect)

    """Fetch the model details in model table and returns the model object data list-
    into caller."""
    def fetchModelDetails(self):
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch the model details in model table.')

            # Query for fetch the car model information from model table
            query = 'SELECT * FROM model'
            cursor.execute(query)
            records = cursor.fetchall()
            logging.info('Successfully fetched the data from model table.')
            cursor.close()

            model_list = []
            for row in records:
                model_id = row[0]
                model_name = row[1]
                price = row[2]
                manufacture_id = row[3]
                carModel = CarModel(model_id, model_name, price, manufacture_id)
                model_list.append(carModel)
            logging.info("Successfully returns the model list to caller.")

            return model_list

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while getting data.', error)

        finally:
            self.close_connection(connect)

    def FetchUpgradeDetails(self, regNo):
        """The selected regNo upgrade details fetch from upgrade table. the selected component names fetches from-
        accessories table."""
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch the upgrade details')

            query = "SELECT component_name from accessorie where component_id in (SELECT component_id from upgrade WHERE reg_no=?)"
            cursor.execute(query, (regNo,))
            record = cursor.fetchall()
            cursor.close()
            logging.info("Fetch the upgrade data successfully")
            # componentNameList = [regNo]
            componentNameList = []
            for row in record:
                componentNameList.append(row[0])
            return componentNameList
        except (Exception, sqlite3.Error) as error:
            logging.error('%s while get component name', error)

        finally:
            self.close_connection(connect)

    # Get the car details in car table
    def fetchCarDetails(self):
        connect = self.get_connection()
        cursor = connect.cursor()
        logging.info('Connect the database successfully for insert value')

        try:
            # Query for fetch the car  information from car table
            query = 'SELECT * FROM car'
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            logging.info('Successfully fetched the data from car table')

            car_list = []
            for row in records:
                reg_no = row[0]
                colour = row[1]
                num_of_doors = row[2]
                model_id = row[3]
                car = Car(reg_no, colour, num_of_doors, model_id)
                car_list.append(car)

            return car_list

        except (Exception, sqlite3.Error) as error:
            logging.error('%s Error while getting data', error)

        finally:
            self.close_connection(connect)

    """Fetch price od particular component that are given by caller from accessorie table.
     the component price will be return to caller."""
    def fetchAccessoriesPrice(self, component_id):
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch the price.')

            # Query for fetch the component price from accessories table.
            query = "select price from accessorie WHERE component_id = ?"
            cursor.execute(query, (component_id,))
            price = cursor.fetchone()
            cursor.close()
            logging.info('Successfully fetched the price from accessorie table adn return the price to caller.')
            return price[0]
        except (Exception, sqlite3.Error) as error:
            logging.error('%s while getting data', error)
        finally:
            self.close_connection(connect)

    """Fetch the car registration number that are no sold from car table. the car object-
    is created add those registration number to that object. when caller call this function,
    the collection of car object returns to it."""
    def fetchAvailableCarRegNO(self):
        connect = None
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch available car')

            # Query fetch the reg no that are not present in sales table.
            query = "select reg_no from car where reg_no not in (select reg_no from sale)"
            cursor.execute(query)
            record = cursor.fetchall()
            cursor.close()
            logging.info('Successfully fetched the data from car table')

            carList = []
            for row in record:
                regNo = row[0]
                car = Car(regNo)
                carList.append(car)

            return carList

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while getting data', error)
        finally:
            self.close_connection(connect)

