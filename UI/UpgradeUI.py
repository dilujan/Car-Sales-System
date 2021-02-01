from tkinter import *
from tkinter.ttk import Combobox

from Controller.OfficeStaff import OfficeStaff
from POJO.Upgrade import Upgrade
from tkinter import messagebox as mb

import abc


class UpgradeUI(abc.ABC):

    # This class is inherited by OfficeStaffUpgrade and SellerUpgrade class.
    # This is an abstract class.

    # Create the upgrade UI
    def __init__(self):

        self.window = Tk()
        self.window.title('Add Upgrade')
        self.window.geometry('350x250+500+250')

        self.lbl_regNo = Label(self.window, text='Reg No')
        self.lbl_metallic_paint = Label(self.window, text='Metallic paint')
        self.lbl_electric_roof_window = Label(self.window, text='Electric roof window')
        self.lbl_leather_seats = Label(self.window, text='Leather seats')

        self.var_metallic_paint = StringVar()
        self.var_electric_roof_window = StringVar()
        self.var_leather_seats = StringVar()

        self.combo_carRegNo = Combobox(self.window, postcommand=self.getCarRegNo)
        self.checkBtn_metallic_paint = Checkbutton(self.window, variable=self.var_metallic_paint, onvalue='acc001')
        self.checkBtn_metallic_paint.deselect()
        self.checkBtn_electric_roof_window = Checkbutton(self.window, variable=self.var_electric_roof_window,
                                                         onvalue='acc002')
        self.checkBtn_electric_roof_window.deselect()
        self.checkBtn_leather_seats = Checkbutton(self.window, variable=self.var_leather_seats, onvalue='acc003')
        self.checkBtn_leather_seats.deselect()

        self.btn_clear = Button(self.window, text='Clear', command=self.clear)
        self.btn_add = Button(self.window, text='Add', command=self.add)
        self.btn_back = Button(self.window, text='Back', command=self.back)

        self.lbl_regNo.grid(row=1, column=1, padx=8, pady=16)
        self.lbl_metallic_paint.grid(row=2, column=1, padx=8, pady=8)
        self.lbl_electric_roof_window.grid(row=3, column=1, padx=8, pady=8)
        self.lbl_leather_seats.grid(row=4, column=1, padx=8, pady=8)
        self.combo_carRegNo.grid(row=1, column=2, pady=8)
        self.checkBtn_metallic_paint.grid(row=2, column=2, pady=8)
        self.checkBtn_electric_roof_window.grid(row=3, column=2, pady=8)
        self.checkBtn_leather_seats.grid(row=4, column=2, pady=8)

        self.btn_back.place(x=32, y=200)
        self.btn_add.place(x=150, y=200)
        self.btn_clear.place(x=255, y=200)

        self.window.mainloop()

    """when user click arrow button of Combobox, the getCarRegNo function will be called.
    it dynamically updates the values with car reg that are not sold, user can be select-
     one of the value from it."""

    # After the user clicks the arrow in the combobox,
    # postcommand that executes the given function (getCarRegNo),
    # before displaying the pop-down list of choices.
    def getCarRegNo(self):
        # Office staff object calls the function getNonSalesCar()
        # It'll return car reg number as list.
        self.combo_carRegNo['values'] = OfficeStaff().getNonSalesCarRegNo()

    def add(self):
        """Get the all necessary component that are selected by user for particular car.
         they are collected to create a upgrade object. finally create the list of upgrade object,
         because each car has many upgrade. finally the list pass to add upgrade function."""

        # Create a an empty accessories upgrade list
        upgradeList = []

        if self.combo_carRegNo.get() == '':
            mb.showwarning('Message from system', "Car's registration number is not selected")

        else:

            # Fetch the all component to upgrade a car that are only checked by user.
            for u in [self.var_metallic_paint, self.var_leather_seats, self.var_electric_roof_window]:

                # check the components id is not empty.
                # Get the component_Id and car reg no.
                # Create a upgrade object add those value
                if u.get() != '' and u.get() != '0':
                    component_Id = u.get()
                    reg_no = self.combo_carRegNo.get()
                    # print(reg_no, component_Id)
                    upgrade = Upgrade(reg_no, component_Id)
                    upgradeList.append(upgrade)

            result = OfficeStaff().addUpgrade(upgradeList)

            if result:
                mb.showinfo('Message from the system', 'Add upgrades successfully on database')
                self.combo_carRegNo.delete(0, 'end')
                self.checkBtn_leather_seats.deselect()
                self.checkBtn_electric_roof_window.deselect()
                self.checkBtn_metallic_paint.deselect()

            else:
                mb.showwarning('Message from the system', 'The selected upgrade already exist for this car. try again')

    def clear(self):
        self.combo_carRegNo.delete(0, 'end')
        self.checkBtn_leather_seats.deselect()
        self.checkBtn_electric_roof_window.deselect()
        self.checkBtn_metallic_paint.deselect()

    @abc.abstractmethod
    def back(self):
        pass
