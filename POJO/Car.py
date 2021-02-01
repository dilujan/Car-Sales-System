class Car:
    def __init__(self, regNo=None, colour=None, num_of_doors=None, modelId=None):
        self.__modelId = modelId
        self.__num_of_doors = num_of_doors
        self.__colour = colour
        self.__regNo = regNo

    def setModelId(self, modelId):
        self.__modelId = modelId

    def getModelId(self):
        return self.__modelId

    def setNumOfDoors(self, numOfDoors):
        self.__num_of_doors = numOfDoors

    def getNumOfDoors(self):
        return self.__num_of_doors

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setRegNo(self, regNo):
        self.__regNo = regNo

    def getRegNo(self):
        return self.__regNo


