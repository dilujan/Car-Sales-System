from tkinter import *

from Controller.OfficeStaff import OfficeStaff
from POJO.Manufacture import Manufacture

from tkinter import messagebox as mb


class ManufactureView:
    # Create the Manufacture UI

    def __init__(self):

        self.window = Tk()
        self.window.title('Add manufacture')
        self.window.geometry('350x200+500+250')

        self.lbl_manufactureId = Label(self.window, text='Manufacture ID')
        self.lbl_manufactureName = Label(self.window, text='Manufacture Name')
        self.fld_manufactureId = Entry(self.window)
        self.fld_manufactureName = Entry(self.window)
        self.btn_clear = Button(self.window, text='Clear', command=self.clear)
        self.btn_add = Button(self.window, text='Add', command=self.add)
        self.btn_back = Button(self.window, text='Back', command=self.back)

        self.lbl_manufactureId.grid(row=1, column=1, padx=8, pady=16)
        self.lbl_manufactureName.grid(row=2, column=1, padx=8, pady=8)
        self.fld_manufactureId.grid(row=1, column=2, pady=8)
        self.fld_manufactureName.grid(row=2, column=2, pady=8)
        self.btn_back.place(x=32, y=150)
        self.btn_add.place(x=150, y=150)
        self.btn_clear.place(x=255, y=150)

        self.window.mainloop()

    """When user click the clear button, it will be clear the value that are store in-
    the entries."""
    def clear(self):
        self.fld_manufactureName.delete(0, 'end')
        self.fld_manufactureId.delete(0, 'end')

    """When user click the add  button the function will be called. the manufacture id and name-
        are fetched from the entries.manufacture object is created and set those values into manufacture object.
        the addManufacture function in OfficeStaff controller class is called and pass the created user object 
         as parameter (OOPS encapsulation). all the control and logic part is handled by the controller 
         class. the addManufacture method use to add new manufacture in our database using their logic. 
         finally the addManufacture function True or false value according the function successfully-
         completed the define implementation."""
    def add(self):

        manufacture = Manufacture(manufactureId=None, manufactureName=None)
        if self.fld_manufactureId.get() == '' or self.fld_manufactureName.get() == '':
            mb.showwarning('Message from system', 'Please give an manufacture ID and manufacture name')
        else:
            manufacture.setManufactureId(self.fld_manufactureId.get())
            manufacture.setManufactureName(self.fld_manufactureName.get())

            output = OfficeStaff().addManufacture(manufacture)

            if output:
                mb.showinfo('Message from system', 'Successfully add manufacture on database')
                self.fld_manufactureName.delete(0, 'end')
                self.fld_manufactureId.delete(0, 'end')
            else:
                mb.showwarning('Message from system', 'The insertion is failed manufacture ID or manufacture name already exit try again')

    """When user click the back button, it destroy the current window and moves to previous-
    window."""
    def back(self):
        self.window.destroy()
        from UI.OfficeStaffDashboard import OfficeStaffDashBoard
        OfficeStaffDashBoard()
