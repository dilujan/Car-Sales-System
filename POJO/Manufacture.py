class Manufacture:
    def __init__(self, manufactureId=None, manufactureName=None):
        self.__manufactureID = manufactureId
        self.__manufactureName = manufactureName

    def setManufactureId(self, manufactureID):
        self.__manufactureID = manufactureID

    def setManufactureName(self, manufacture_name):
        self.__manufactureName = manufacture_name

    def getManufactureId(self):
        return self.__manufactureID

    def getManufactureName(self):
        return self.__manufactureName


