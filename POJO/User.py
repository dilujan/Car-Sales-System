class User:
    def __init__(self):
        self.__uName = None
        self.__password = None
        self.__roll = None

    def setUserName(self, uName):
        self.__uName = uName

    def getUserName(self):
        return self.__uName

    def setPassword(self, pwd):
        self.__password = pwd

    def getPassword(self):
        return self.__password

    def setRoll(self, roll):
        self.__roll = roll

    def getRoll(self):
        return self.__roll

