from Controller.Staff import Staff
from Model.SellerDAO import SellerDAO


class Seller(Staff):
    """This is the controller class. it inherit from staff class. it communicate with DAO class."""

    # create DAO object in SellerDAO class
    def __init__(self):
        self.sellerDao = SellerDAO()
        super().__init__()

    # create select car method to sell car
    def selectedCarDetails(self, car):
        """The seller can be call this method to get the selected car details. this class's-
         method contact the model class and get the particular information from database."""
        details = self.sellerDao.carData(car.getRegNo())

        # get the output information from encapsulate details list and add to it return list
        returnList = [
            details[0].getRegNo(),
            details[0].getColour(),
            details[0].getNumOfDoors(),
            details[1].getModelName(),
            details[2].getManufactureName()
        ]

        return returnList

    # create selected car upgrade details method to get upgrade details of sell car
    def selectedCarUpgradeDetails(self, car):
        """The seller can be call this method to get the selected car upgraded details. this class's-
         method contact the model class and get the particular information from database."""
        componentNameList = self.staffDao.FetchUpgradeDetails(car.getRegNo())
        return componentNameList

    # create selected car price method to final amount of sell car
    def selectCarPrice(self, car):
        """When call this method it contact with DAO class to get the final price of selected car"""

        # Create a result variable to store the upgrade object.
        # Call the fetchSumOfUpgradePrice in DAO class and pass the selected car registration-
        # number to get the sum of selected car upgrades price.
        upgrade = self.sellerDao.fetchSumOfUpgradePrice(car.getRegNo())

        # Get the sum of upgrade price from upgrade object.
        # If the sum of upgrade price is none, then it will change to zero
        if upgrade.getPrice() is None:
            upgradePrice = 0
        else:
            upgradePrice = upgrade.getPrice()

        carPrice = self.sellerDao.fetchCarPrice(car.getRegNo())

        return upgradePrice + carPrice

    # Create new sale method to store the sell car details.
    def addNewSale(self, sale):
        result = self.insertDB.insertValues(sale.getTimeStamp(), sale.getFinalAmount(), sale.getInitialCurrencyType(),
                                            sale.getInitialCurrency(), sale.getRegNo(), tbName='sale')
        return result
