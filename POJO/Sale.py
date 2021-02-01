class Sale:
    def __init__(self, sale_id=None, time_stamp=None, final_amount=None, initial_currencyType=None,
                 initial_currency=None, regNo=None):
        self.__sale_id = sale_id
        self.__time_stamp = time_stamp
        self.__final_amount = final_amount
        self.__initial_currencyType = initial_currencyType
        self.__initial_currency = initial_currency
        self.__regNo = regNo

    def setSaleId(self, saleId):
        self.__sale_id = saleId

    def setTimeStamp(self, timeStamp):
        self.__time_stamp = timeStamp

    def setFinalAmount(self, finalAmount):
        self.__final_amount = finalAmount

    def setInitialCurrencyType(self, cType):
        self.__initial_currencyType = cType

    def setInitialCurrency(self, iCurrency):
        self.__initial_currency = iCurrency

    def setRegNo(self, regNo):
        self.__regNo = regNo

    def getSaleId(self):
        return self.__sale_id

    def getTimeStamp(self):
        return self.__time_stamp

    def getFinalAmount(self):
        return self.__final_amount

    def getInitialCurrencyType(self):
        return self.__initial_currencyType

    def getRegNo(self):
        return self.__regNo

    def getInitialCurrency(self):
        return self.__initial_currency
