class CarModel:
    def __init__(self, modelId=None, modelName=None, price=None, manufactureId=None):
        self.__price = price
        self.__modelName = modelName
        self.__modelId = modelId
        self.__manufactureID = manufactureId

    def setManufactureId(self, manufactureID):
        self.__manufactureID = manufactureID

    def setModelId(self, modelId):
        self.__modelId = modelId

    def setModelName(self, modelName):
        self.__modelName = modelName

    def setPrice(self, price):
        self.__price = price

    def getManufactureId(self):
        return self.__manufactureID

    def getModelId(self):
        return self.__modelId

    def getModelName(self):
        return self.__modelName

    def getPrice(self):
        return self.__price



