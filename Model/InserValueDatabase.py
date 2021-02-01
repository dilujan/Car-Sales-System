import logging
import sqlite3

from Model.DB_connection import DB_connection

logging.basicConfig(filename='../logging.log', filemode='w', format='%(asctime)s - %(levelname)s -%(message)s',
                    level=logging.INFO)


class InsertValueDatabase(DB_connection):

    """This method to use to insert data value into database, when any of InsertValueDatabase object
    call this function. when call this function must be pass two parameter
                *args :- Which values to insert database.
                tbName :- The name of the table to insert those values.
    Here, OOPS method overloading concept is used, because same method is called to insert the values
    any table but that depend on number of table column (Field values)."""

    # *args in function is used to pass a variable number of arguments (Data values) to a function.
    # tbName is table of the name.
    def insertValues(self, *args, tbName):
        try:
            # Call the parent class get_connection() method to connect the database.
            connect = self.get_connection()
            connect.execute('PRAGMA foreign_keys = on')
            cursor = connect.cursor()
            logging.info('Connect the database successfully for insert value')

            # The insert values into table that are determine by arguments(Values).
            if len(args) == 2:
                query = 'insert into {} values (?,?)'.format(tbName)
                cursor.execute(query, (args[0], args[1]))
                connect.commit()
                logging.info('Record inserted successfully into {} table'.format(tbName))
                cursor.close()

            elif len(args) == 3:
                query = 'insert into {} values (?,?,?)'.format(tbName)
                cursor.execute(query, (args[0], args[1], args[2]))
                connect.commit()
                logging.info('Record inserted successfully into {} table'.format(tbName))
                cursor.close()

            elif len(args) == 4:
                query = 'insert into {} values (?,?,?,?)'.format(tbName)
                cursor.execute(query, (args[0], args[1], args[2], args[3]))
                connect.commit()
                logging.info('Record inserted successfully into {} table'.format(tbName))
                cursor.close()

            elif len(args) == 5:
                # This is for insert into sales table, because the sales id auto increases.
                query = 'insert into {}(time_stamp,final_amount,inital_currency_type,inital_currency,reg_no) values (?,?,?,?,?)'.format(tbName)
                cursor.execute(query, (args[0], args[1], args[2], args[3], args[4]))
                connect.commit()
                logging.info('Record inserted successfully into {} table'.format(tbName))
                cursor.close()

        except (Exception, sqlite3.Error) as error:
            logging.error('Failed to insert data into {} table'.format(tbName))
            logging.error("Exception class is: {}".format(error.__class__))
            logging.error("Exception is {}".format(error.args))

            # If any problem occurs, it return False boolean value to caller.
            return False

        else:
            # If the insertion function successfully completed, the method return True -
            # statement into caller function.
            return True

        finally:
            # Call the parent class close connection function to disconnect the database connection.
            self.close_connection(connect)
