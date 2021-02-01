from tkinter import *

from UI.CarModelUI import CarModelUI
from UI.CarUI import CarUI
from UI.DeleteCarUI import DeleteCarUI
from UI.ManufactureUI import ManufactureView
from UI.OffficeStaffUpgradeUI import OfficeStaffUpgradeUI
from UI.SearchCar import SearchCar
from UI.SoldCarUI import SoldCarUI


class OfficeStaffDashBoard:

    # Office staff dash board UI design
    def __init__(self):

        self.window = Tk()
        self.window.title('Staff Dash bord')
        self.window.geometry('350x300+500+250')

        self.btn_addManufacture = Button(self.window, text='Add Manufacture',
                                         command=lambda: self.clickDashboardBtn('btn_addManufacture'))
        self.btn_addModel = Button(self.window, text='Add Model', width=14,
                                   command=lambda: self.clickDashboardBtn('btn_addModel'))
        self.btn_addCar = Button(self.window, text='Add Car', width=14,
                                 command=lambda: self.clickDashboardBtn('btn_addCar'))
        self.btn_addUpgrade = Button(self.window, text='Add Upgrade', width=14,
                                     command=lambda: self.clickDashboardBtn('btn_addUpgrade'))
        self.btn_deleteCar = Button(self.window, text='Delete Car', width=14,
                                    command=lambda: self.clickDashboardBtn('btn_deleteCar'))
        self.btn_searchCar = Button(self.window, text='Search Car', width=14,
                                    command=lambda: self.clickDashboardBtn('btn_searchCar'))
        self.btn_viewSoldCar = Button(self.window, text='View Sold Car', width=14,
                                      command=lambda: self.clickDashboardBtn('btn_viewSoldCar'))
        self.btn_logout = Button(self.window, text='Logout', width=14,
                                 command=lambda: self.clickDashboardBtn('btn_logout'))

        self.btn_addManufacture.grid(row=1, column=1, padx=16, pady=16)
        self.btn_addModel.grid(row=1, column=2, padx=16, pady=16)
        self.btn_addCar.grid(row=2, column=1, padx=16, pady=16)
        self.btn_addUpgrade.grid(row=2, column=2, padx=16, pady=16)
        self.btn_deleteCar.grid(row=3, column=1, padx=16, pady=16)
        self.btn_searchCar.grid(row=3, column=2, padx=16, pady=16)
        self.btn_viewSoldCar.grid(row=4, column=1, padx=16, pady=16)
        self.btn_logout.grid(row=4, column=2, padx=16, pady=16)

        self.window.mainloop()

    """When user click the particular action button, clickDashboardBtn that is defined in lambda-
     will be called. it has buttonId as argument. the function decides which task will be opened-
     according the button id."""
    def clickDashboardBtn(self, buttonId):
        if buttonId == 'btn_addManufacture':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open an add manufacture view
            ManufactureView()

        elif buttonId == 'btn_addModel':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open an add model view
            CarModelUI()

        elif buttonId == 'btn_addCar':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open an add car view
            CarUI()

        elif buttonId == 'btn_addUpgrade':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open the car upgrade view
            OfficeStaffUpgradeUI()

        elif buttonId == 'btn_deleteCar':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open a  car delete view
            DeleteCarUI()

        elif buttonId == 'btn_searchCar':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open a search car view
            SearchCar()

        elif buttonId == 'btn_viewSoldCar':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open a view sold car view
            SoldCarUI()

        elif buttonId == 'btn_logout':
            # Destroy the office dashboard view
            self.window.destroy()
            # Open a login view
            from UI.LoginUI import LoginView
            LoginView()




