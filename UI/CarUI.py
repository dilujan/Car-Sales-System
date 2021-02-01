from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

from Controller.OfficeStaff import OfficeStaff
from POJO.Car import Car
from POJO.CarModel import CarModel


class CarUI:

    # Create a Car UI
    def __init__(self):

        self.window = Tk()
        self.window.title('Add Car')
        self.window.geometry('350x250+500+250')

        self.lbl_regNo = Label(self.window, text='Reg No')
        self.lbl_colour = Label(self.window, text='Colour')
        self.lbl_numOfDoors = Label(self.window, text='Num of doors')
        self.lbl_modelId = Label(self.window, text='Model Name')

        self.fld_regNo = Entry(self.window)
        self.fld_colour = Entry(self.window)
        self.fld_numOfDoors = Entry(self.window)
        self.combo_modelName = Combobox(self.window, postcommand=self.getModelName)

        self.btn_clear = Button(self.window, text='Clear', command=self.clear)
        self.btn_add = Button(self.window, text='Add', command=self.add)
        self.btn_back = Button(self.window, text='Back', command=self.back)

        self.lbl_regNo.grid(row=1, column=1, padx=8, pady=16)
        self.lbl_colour.grid(row=2, column=1, padx=8, pady=8)
        self.lbl_numOfDoors.grid(row=3, column=1, padx=8, pady=8)
        self.lbl_modelId.grid(row=4, column=1, padx=8, pady=8)
        self.fld_regNo.grid(row=1, column=2, pady=8)
        self.fld_colour.grid(row=2, column=2, pady=8)
        self.fld_numOfDoors.grid(row=3, column=2, pady=8)
        self.combo_modelName.grid(row=4, column=2, pady=8)

        self.btn_back.place(x=32, y=200)
        self.btn_add.place(x=150, y=200)
        self.btn_clear.place(x=255, y=200)

        self.window.mainloop()

    """when user click arrow button of Combobox, the getModelName function will be called.
         it dynamically updates the values with model name from model table,
        user can be select one of the value from it."""

    # After the user clicks the arrow in the combobox,
    # postcommand that executes the given function (getModelName),
    # before displaying the pop-down list of choices.
    def getModelName(self):
        # Office staff object calls the function getModelName()
        # It'll return model name as list.
        self.combo_modelName['values'] = OfficeStaff().getModelName()

    def clear(self):
        self.fld_regNo.delete(0, 'end')
        self.fld_colour.delete(0, 'end')
        self.fld_numOfDoors.delete(0, 'end')
        self.combo_modelName.delete(0, 'end')

    def add(self):
        if self.fld_regNo.get() == '' or self.fld_colour.get() == '' or self.fld_numOfDoors.get() == '' or self.combo_modelName.get() == '':
            mb.showwarning('Message from system', 'Some field values are empty, check it.')
        else:
            # Covert the model name to model Id
            modelId = OfficeStaff().covert_modelId(self.combo_modelName.get())

            # Read the value from each input from user that will add to car class
            car = Car(self.fld_regNo.get(), self.fld_colour.get(), self.fld_numOfDoors.get(), modelId)

            # Call the add car function from office staff class and pass carModel object
            # The return value store in output variable
            output = OfficeStaff().addCar(car)

            if output:
                mb.showinfo('Message from system', 'Successfully add car on database')
                self.fld_regNo.delete(0, 'end')
                self.fld_colour.delete(0, 'end')
                self.fld_numOfDoors.delete(0, 'end')
                self.combo_modelName.delete(0, 'end')

            else:
                mb.showwarning('Message from system', 'The insertion is failed registration number already exist. try again')

    def back(self):
        self.window.destroy()
        from UI.OfficeStaffDashboard import OfficeStaffDashBoard
        OfficeStaffDashBoard()
