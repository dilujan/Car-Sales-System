from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

from Controller.Seller import Seller
from POJO.Car import Car
from UI.SaleView import SaleView
from UI.SellerUpgradeUI import SellerUpgradeUI
from UI.UpgradeUI import UpgradeUI


class SellerDashboard:

    # Create a seller UI
    def __init__(self):
        self.window = Tk()
        self.window.title('Select car for sale')
        self.window.geometry('350x300+500+250')

        self.lbl_selectCar = Label(self.window, text='Select Car')
        self.combo_selectCar = Combobox(self.window, postcommand=self.chooseCar)

        self.btn_viewCarDetails = Button(self.window, text='Selected Car details', command=self.carDetails)
        self.btn_viewCarUpgrades = Button(self.window, text='Selected Car upgrades', command=self.showUpgrades)
        self.btn_addCarUpgrades = Button(self.window, text='Add new upgrades', command=self.addUpgrades)

        self.btn_saleCar = Button(self.window, text='Sale car', command=self.saleCar)
        self.btn_logout = Button(self.window, text='Logout', command=self.logout)
        self.btn_clear = Button(self.window, text='Clear', command=self.clear)

        self.lbl_selectCar.grid(row=1, column=1, padx=8, pady=16)
        self.combo_selectCar.grid(row=1, column=2, padx=8, pady=16)
        self.btn_viewCarDetails.grid(row=2, column=2, padx=8, pady=16)
        self.btn_viewCarUpgrades.grid(row=3, column=2, padx=8, pady=16)
        self.btn_addCarUpgrades.grid(row=4, column=2, padx=8, pady=16)

        self.btn_logout.grid(row=5, column=1)
        self.btn_saleCar.grid(row=5, column=2)
        self.btn_clear.grid(row=5, column=3)

        self.window.mainloop()

    def chooseCar(self):
        """When user click the combobox arrow, this function will be called and show-
        the car registration number that are store in the list dynamically. the function-
        call another function in seller class (Controller class) to update the values-
        attribute."""

        # The getNonSalesCarRegNo() method returns cars that are not sold
        self.combo_selectCar['values'] = Seller().getNonSalesCarRegNo()

    def carDetails(self):
        """The user want to get the details of the selected car. he can press the Selected Car upgrades-
        button when the function will be called. it calls the function in seller to update the selected
        car upgrade information."""

        if self.combo_selectCar.get() == '':
            mb.showwarning('Message from system', 'Please select one of car above')
        else:
            car = Car()
            car.setRegNo(self.combo_selectCar.get())
            carRecord = Seller().selectedCarDetails(car)

            tempWindow = Tk()
            tempWindow.title('Selected car details')
            for i in range(len(carRecord)):
                tempEntry = Entry(tempWindow, width=20, fg='blue',
                                  font=('Arial', 16, 'bold'))
                tempEntry.grid(row=i, column=0)
                tempEntry.insert(END, carRecord[i])
            tempWindow.mainloop()

    def showUpgrades(self):
        """The user want to get the upgraded details of the selected car. he can press the Selected Car details-
            button when the function will be called. it calls the function in seller to update the selected
            car information."""

        if self.combo_selectCar.get() == '':
            mb.showwarning('Message from system', 'Please select one of car above')
        else:
            car = Car()
            car.setRegNo(self.combo_selectCar.get())
            upgradeRecord = Seller().selectedCarUpgradeDetails(car)

            tempWindow = Tk()
            tempWindow.title('Selected car upgraded details')

            for i in range(len(upgradeRecord)):
                tempEntry = Entry(tempWindow, width=20, fg='blue',
                                  font=('Arial', 16, 'bold'))
                tempEntry.grid(row=i, column=0)
                tempEntry.insert(END, upgradeRecord[i])
            tempWindow.mainloop()

    def addUpgrades(self):
        """The user wants to add new upgrades for selected car the SellerUpgrades UI will be opened.
        it inherit UpgradeUI class."""
        self.window.destroy()
        SellerUpgradeUI()

    def saleCar(self):
        """When press the sale button, the method will be called. this open a new window to confirm sell-
        the selected car. this automatically add the selected car and final amount on newly open window."""
        if self.combo_selectCar.get() == '':
            mb.showwarning('Message from system', 'Please select one of car above')
        else:
            car = Car(self.combo_selectCar.get())
            finalPrice = Seller().selectCarPrice(car)
            SaleView(self.combo_selectCar.get(), finalPrice)
            # self.combo_selectCar.delete(0, 'end')

    def logout(self):
        # Destroy the seller dashboard view
        self.window.destroy()
        # Open a logout view
        from UI.LoginUI import LoginView
        LoginView()

    def clear(self):
        self.combo_selectCar.delete(0, 'end')

