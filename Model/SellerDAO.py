import logging
import sqlite3

from Model.DB_connection import DB_connection
from POJO.Car import Car
from POJO.CarModel import CarModel
from POJO.Manufacture import Manufacture
from POJO.Upgrade import Upgrade

logging.basicConfig(filename='../logging.log', filemode='w', format='%(asctime)s - %(levelname)s -%(message)s',
                    level=logging.INFO)


class SellerDAO(DB_connection):

    def carData(self, regNo):
        """The selected car car data fetches from database using this method. """
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info('Connect the database successfully for fetch the car data')

            query = "SELECT car.reg_no, colour, num_of_doors, model_name, manufacture_name from car, model, manufacture WHERE car.model_id = model.model_id and model.manufacture_id = manufacture.manufacture_id and reg_no = ?"
            cursor.execute(query, (regNo,))
            record = cursor.fetchall()
            cursor.close()
            logging.info("Fetch the car data successfully")

            # create car, model, manufacture object to encapsulate fetch the values from database
            car = Car(record[0][0], record[0][1], record[0][2])
            model = CarModel(modelName=record[0][3])
            manufacture = Manufacture(manufactureName=record[0][4])

            # create a list and add those object into this list and returns to caller.
            detailsList = [car, model, manufacture]
            return detailsList

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while get car data', error)

        finally:
            self.close_connection(connect)

    # def UpgradeDetails(self, regNo):
    #     try:
    #         connect = self.get_connection()
    #         cursor = connect.cursor()
    #         logging.info('Connect the database successfully for fetch the upgrade details')
    #
    #         query = "SELECT component_name from accessorie where component_id in (SELECT component_id from upgrade WHERE reg_no=?)"
    #         cursor.execute(query, (regNo,))
    #         record = cursor.fetchall()
    #         cursor.close()
    #         logging.info("Fetch the upgrade data successfully")
    #         componentNameList = [regNo]
    #         for row in record:
    #             componentNameList.append(row[0])
    #         return componentNameList
    #     except (Exception, sqlite3.Error) as error:
    #         logging.error('%s while get component name', error)
    #
    #     finally:
    #         self.close_connection(connect)

    def fetchSumOfUpgradePrice(self, regNo):
        """This method fetch the total price of selected car from upgrade table."""
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info("Connect the database successfully for fetch the car's upgrade price")

            query = "SELECT sum(final_price) from upgrade WHERE reg_no=?"
            cursor.execute(query, (regNo,))
            record = cursor.fetchall()
            cursor.close()
            logging.info("Fetch the sum of price successfully")

            upgrade = Upgrade(price=record[0][0])

            return upgrade

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while get price data', error)

        finally:
            self.close_connection(connect)

    def fetchCarPrice(self, regNo):
        """The method fetch the price from car model table in database-
         for car that are selected by user."""
        try:
            connect = self.get_connection()
            cursor = connect.cursor()
            logging.info("Connect the database successfully for fetch the car's model price")

            query = "SELECT price from model WHERE model_id in (SELECT model_id from car WHERE reg_no = ?)"
            cursor.execute(query, (regNo,))
            price = cursor.fetchall()
            cursor.close()
            logging.info("Fetch the car price successfully")

            return price[0][0]

        except (Exception, sqlite3.Error) as error:
            logging.error('%s while get car price', error)

        finally:
            self.close_connection(connect)









