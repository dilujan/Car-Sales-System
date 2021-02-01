from Model.InserValueDatabase import InsertValueDatabase
from Model.OfficeStaffDao import OfficeStaffDao
from Model.StaffDao import StaffDao


class Staff:
    """It is parent class for office staff and seller. It controls the all logic activity (function)-
    that are made by office staff and seller. It is the intermediate class between staff function-
    (activities) UI and the backend class (model class) of StaffDao()."""

    # Create the parent constructor (Staff class).
    # Create the StaffDao object for communicate the backend.
    # Create the insertValue object for communicate the backend to call the insert value method.
    def __init__(self):
        self.__result = None
        self.staffDao = StaffDao()
        self.insertDB = InsertValueDatabase()

    def getManufactureName(self):
        """Get the all manufacture name from model class (backend) and-
         return the manufacture name list for caller."""

        # Call the getManufactureDetails() in staffDao model class to get the manufacture details.
        # It returns the list of manufacture object.
        manufactureList = self.staffDao.fetchManufactureDetails()

        manufactureNameList = []
        for i in manufactureList:
            # Fetch the manufacture name from each manufacture object.
            # Add those name into manufactureNameList.
            manufactureNameList.append(i.getManufactureName())
        return manufactureNameList

    def covert_manufactureId(self, manufactureName):
        """convert specify manufacture name to manufacture id. If name of the manufacture-
        object is equals to manufacture name that is given by user, it will returns-
        the particular manufacture id of the manufacture name."""

        # Call the getManufactureDetails() in model class to get the manufacture details.
        manufactureList = self.staffDao.fetchManufactureDetails()

        for i in manufactureList:
            # Check the manufacture name of the object in list.
            # If true, it returns the manufacture id.

            if i.getManufactureName() == manufactureName:
                # It returns the particular manufacture id
                return i.getManufactureId()

    def getModelName(self):
        """Get the all car model name from staffDao model class and return the model name list for caller."""

        # Call the getModelDetails() in staffDao model class to get the model details.
        # It returns the list of model object.
        modelList = self.staffDao.fetchModelDetails()

        modelNameList = []
        for i in modelList:
            # Fetch the model name from each model object.
            # Add those name into modelNameList.
            modelNameList.append(i.getModelName())
        return modelNameList

    def covert_modelId(self, modelName):
        """Convert specify manufacture name to manufacture manufacture id and returns the id to-
        caller."""

        # Get the all car model details from model class
        modelList = self.staffDao.fetchModelDetails()

        for i in modelList:
            # Check the manufacture name in the table equals to given name
            if i.getModelName() == modelName:
                # It returns the particular manufacture id
                return i.getModelId()

    def getCarRegNo(self):
        """Get the all car reg no from staffDao model class and return the reg number list for caller."""

        carList = self.staffDao.fetchCarDetails()
        regNoList = []
        for car in carList:
            regNoList.append(car.getRegNo())
        return regNoList

    # Create a method non sales car list from data model class.
    def getNonSalesCarRegNo(self):
        """The method update the car registration number that are not sale."""
        carList = self.staffDao.fetchAvailableCarRegNO()
        regNoList = []
        for car in carList:
            regNoList.append(car.getRegNo())
        return regNoList

    # Create an add upgrade function
    def addUpgrade(self, upgrade):
        """Get the price of particular component from model class and add those price to upgraded car"""

        # uCar :- upgraded car object that are selected by user.
        # Get the price of each component that are selected by user to upgrade car.
        for uCar in upgrade:
            price = self.staffDao.fetchAccessoriesPrice(uCar.getComponentId())
            self.__result = self.insertDB.insertValues(uCar.getRegNo(),
                                                       uCar.getComponentId(), price, tbName='upgrade')
            if not self.__result:
                break
        return self.__result






