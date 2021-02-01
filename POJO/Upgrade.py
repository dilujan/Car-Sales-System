class Upgrade:
    def __init__(self, regNo=None, component_id=None, price=None):
        self.__regNo = regNo
        self.__component_id = component_id
        self.__price = price

    def setRegNo(self, regNo):
        self.__regNo = regNo

    def setComponentId(self, component_id):
        self.__component_id = component_id

    def setPrice(self, price):
        self.__price = price

    def getRegNo(self):
        return self.__regNo

    def getComponentId(self):
        return self.__component_id

    def getPrice(self):
        return self.__price

