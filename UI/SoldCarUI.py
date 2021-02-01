from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

from Controller.OfficeStaff import OfficeStaff
from POJO.Car import Car


class SoldCarUI:

    # Create sold car UI
    def __init__(self):
        self.window = Tk()
        self.window.title('Sold car')
        self.window.geometry('350x200+500+250')

        self.lbl_selectCar = Label(self.window, text='Select car')
        self.combo_selectCar = Combobox(self.window, postcommand=self.getCar)

        self.lbl_showUpgrades = Label(self.window, text='Upgrades')
        self.fld_showUpgrades = Entry(self.window)

        self.lbl_showFinalPrice = Label(self.window, text='Final price')
        self.fld_showFinalPrice = Entry(self.window)

        self.btn_clear = Button(self.window, text='Clear', command=self.clear)
        self.btn_search = Button(self.window, text='Show', command=self.search)
        self.btn_back = Button(self.window, text='Back', command=self.back)

        self.lbl_selectCar.grid(row=1, column=1, padx=8, pady=16)
        self.combo_selectCar.grid(row=1, column=2, padx=8, pady=16)

        self.lbl_showUpgrades.grid(row=2, column=1, padx=8, pady=16)
        self.fld_showUpgrades.grid(row=2, column=2, padx=8, pady=16)

        self.lbl_showFinalPrice.grid(row=3, column=1, padx=8, pady=16)
        self.fld_showFinalPrice.grid(row=3, column=2, padx=8, pady=16)

        self.btn_back.place(x=32, y=150)
        self.btn_search.place(x=150, y=150)
        self.btn_clear.place(x=255, y=150)

        self.window.mainloop()

    def getCar(self):
        self.combo_selectCar['values'] = OfficeStaff().getSoldCarRegNo()

    def clear(self):
        self.fld_showUpgrades.delete(0, 'end')
        self.fld_showFinalPrice.delete(0, 'end')

    def search(self):
        """Call the viewSoldCarDetails method from controller class and get all sold car details
        finally add those values into particular entries. the for loops use for enter the upgrades-
        values one by one into entries."""
        if self.combo_selectCar.get() == '':
            mb.showwarning('Message from system', 'Please select one car above')
        else:
            car = Car(regNo=self.combo_selectCar.get())
            soldCarDetails = OfficeStaff().viewSoldCarDetails(car)
            self.fld_showFinalPrice.insert(END, soldCarDetails[1])
            # for i in range(1, len(soldCarDetails[0])):
            #     self.fld_showUpgrades.insert(END, soldCarDetails[0][i])
            #     self.fld_showUpgrades.insert(END, ',')
            for i in soldCarDetails[0]:
                self.fld_showUpgrades.insert(END, i)
                self.fld_showUpgrades.insert(END, ',')

    def back(self):
        self.window.destroy()
        from UI.OfficeStaffDashboard import OfficeStaffDashBoard
        OfficeStaffDashBoard()
