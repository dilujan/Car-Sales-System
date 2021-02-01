from Controller.Staff import Staff
from Model.OfficeStaffDao import OfficeStaffDao


class OfficeStaff(Staff):
    """This is the controller class. it inherit from staff class. it communicate with DAO class."""

    # create DAO object in OfficeStaffDao class
    def __init__(self):
        self.officeStaffDao = OfficeStaffDao()
        super().__init__()

    # create add manufacture method
    def addManufacture(self, manufacture):
        """Call the insert value method in model class, pass the values that are get from-
        manufacture object to add database."""
        self.__result = self.insertDB.insertValues(manufacture.getManufactureId(), manufacture.getManufactureName(),
                                                   tbName='manufacture')
        return self.__result

    # Create add car model method
    def addModel(self, carModel):
        self.__result = self.insertDB.insertValues(carModel.getModelId(), carModel.getModelName(), carModel.getPrice(),
                                                   carModel.getManufactureId(), tbName='model')
        return self.__result

    # Create add car method
    def addCar(self, car):
        self.__result = self.insertDB.insertValues(car.getRegNo(), car.getColour(), car.getNumOfDoors(),
                                                   car.getModelId(),
                                                   tbName='car')
        return self.__result

    # Create delete car method
    def deleteCar(self, car):
        self.__result = self.officeStaffDao.remove_car(car.getRegNo())
        return self.__result

    # create search car method.
    def searchCar(self, modelName, manufactureName):
        """When user click the search button according the argument type, the implementation-
         will be selected. the implementation call the model class method to get the information-
         from database"""

        # If the modeName is not null and manufactureName is null, the output search car result-
        # will be under the model name.
        if modelName != '' and manufactureName == '':
            return self.officeStaffDao.carData(modelName)

        # If the modeName is null and manufactureName is not null, the output search car result-
        # will be under the manufacture name.
        elif modelName == '' and manufactureName != '':
            return self.officeStaffDao.carData(manufactureName=manufactureName)

        # If the both names are not null, the search result will be under the model name and-
        # manufacture name.
        elif modelName != '' and manufactureName != '':
            return self.officeStaffDao.carData(modelName, manufactureName)

    # Get the registration number of sold cars
    def getSoldCarRegNo(self):
        """sold car's registration numbers will be get from subtract the available car's-
         registration numbers."""
        carRegNo = self.getCarRegNo()
        availableCarRegNO = self.getNonSalesCarRegNo()
        soldCarRegNo = list(set(carRegNo) - set(availableCarRegNO))
        return soldCarRegNo

    # Get the view sold car details
    def viewSoldCarDetails(self, car):
        """The selected car information get from car object and pass into model class to-
        get the upgrades and final amount of sold cars."""
        upgradeDetails = self.staffDao.FetchUpgradeDetails(car.getRegNo())
        finalAmount = self.officeStaffDao.fetchSoldCarFinalAmount(car.getRegNo())
        viewSoldCarDetailsList = [upgradeDetails, finalAmount]
        return viewSoldCarDetailsList
