from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

from Controller.OfficeStaff import OfficeStaff
from POJO.CarModel import CarModel


class CarModelUI:

    # Create the car model UI

    def __init__(self):

        self.window = Tk()
        self.window.title('Add Model')
        self.window.geometry('350x250+500+250')

        self.lbl_modelId = Label(self.window, text='Model ID')
        self.lbl_modelName = Label(self.window, text='Model Name')
        self.lbl_price = Label(self.window, text='Price')
        self.lbl_manufacture = Label(self.window, text='Select manufacture')

        self.fld_modelId = Entry(self.window)
        self.fld_modelName = Entry(self.window)
        self.fld_price = Entry(self.window)
        self.combo_manufacture = Combobox(self.window, postcommand=self.getManufactureName)

        self.btn_clear = Button(self.window, text='Clear', command=self.clear)
        self.btn_add = Button(self.window, text='Add', command=self.add)
        self.btn_back = Button(self.window, text='Back', command=self.back)

        self.lbl_modelId.grid(row=1, column=1, padx=8, pady=16)
        self.lbl_modelName.grid(row=2, column=1, padx=8, pady=8)
        self.lbl_price.grid(row=3, column=1, padx=8, pady=8)
        self.lbl_manufacture.grid(row=4, column=1, padx=8, pady=8)
        self.fld_modelId.grid(row=1, column=2, pady=8)
        self.fld_modelName.grid(row=2, column=2, pady=8)
        self.fld_price.grid(row=3, column=2, pady=8)
        self.combo_manufacture.grid(row=4, column=2, pady=8)

        self.btn_back.place(x=32, y=200)
        self.btn_add.place(x=150, y=200)
        self.btn_clear.place(x=255, y=200)

        self.window.mainloop()

    """when user click arrow button of Combobox, the getManufacture function will be called.
     it dynamically updates the values with manufacture name from manufacture table,
    user can be select one of the value from it."""

    # After the user clicks the arrow in the combobox,
    # postcommand that executes the given function (getManufactureName),
    # before displaying the pop-down list of choices.
    def getManufactureName(self):
        # Office staff object calls the function getManufactureName()
        # It'll return manufacture name as list.
        self.combo_manufacture['values'] = OfficeStaff().getManufactureName()

    def clear(self):
        self.fld_modelId.delete(0, 'end')
        self.fld_price.delete(0, 'end')
        self.fld_modelName.delete(0, 'end')
        self.combo_manufacture.delete(0, 'end')

    """When user click the add button, the function will be called. first it convert manufacture name-
    into manufacture id to store model table. CarModel object is  created and pass those values-
    that are fetch from each entries. call the addModel in office staff controller class. 
    pass the object that was created as argument."""
    def add(self):
        if self.fld_modelName.get() == '' or self.fld_modelName.get() == '' or self.fld_price.get() == '' or self.combo_manufacture.get() == '':
            mb.showwarning('Message from system', 'Some field values are empty, check it.')
        else:
            # Covert the manufacture name to manufacture Id
            manufactureId = OfficeStaff().covert_manufactureId(self.combo_manufacture.get())

            # Read the value from each input from user that will add to car model class
            carModel = CarModel(self.fld_modelId.get(), self.fld_modelName.get(), self.fld_price.get(),
                                manufactureId)

            # Call the add car function from office staff class and pass carModel object
            # The return value (True or false) store in output variable
            output = OfficeStaff().addModel(carModel)

            if output:
                mb.showinfo('Message from system', 'Successfully add model on database')
                self.fld_modelId.delete(0, 'end')
                self.fld_modelName.delete(0, 'end')
                self.fld_price.delete(0, 'end')
                self.combo_manufacture.delete(0, 'end')

            else:
                mb.showwarning('Message from system', 'The insertion is failed the model id or model name already exit. try again')

    def back(self):
        self.window.destroy()
        from UI.OfficeStaffDashboard import OfficeStaffDashBoard
        OfficeStaffDashBoard()
