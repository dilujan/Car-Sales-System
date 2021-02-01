from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

from Controller.OfficeStaff import OfficeStaff
from POJO.Car import Car


class DeleteCarUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Delete Car')
        self.window.geometry('350x200+500+250')

        self.lbl_selectCar = Label(self.window, text='select car')
        self.combo_selectCar = Combobox(self.window, postcommand=self.getCarRegNo)

        self.btn_clear = Button(self.window, text='Clear', command=self.clear)
        self.btn_delete = Button(self.window, text='Delete', command=self.delete)
        self.btn_back = Button(self.window, text='Back', command=self.back)

        self.lbl_selectCar.grid(row=1, column=1, padx=8, pady=16)
        self.combo_selectCar.grid(row=1, column=2, padx=8, pady=16)
        self.btn_back.place(x=32, y=150)
        self.btn_delete.place(x=150, y=150)
        self.btn_clear.place(x=255, y=150)

        self.window.mainloop()

    def getCarRegNo(self):
        self.combo_selectCar['values'] = OfficeStaff().getNonSalesCarRegNo()

    def clear(self):
        self.combo_selectCar.delete(0, 'end')

    def delete(self):
        if self.combo_selectCar.get() == '':
            mb.showwarning('Message from system', 'The car not selected')
        else:

            car = Car(regNo=self.combo_selectCar.get())

            output = OfficeStaff().deleteCar(car)
            if output:
                mb.showinfo('Message from system', 'Successfully deleted car')
                self.combo_selectCar.delete(0, 'end')
            else:
                mb.showwarning('Message from system', 'The operation failed')

    def back(self):
        self.window.destroy()
        from UI.OfficeStaffDashboard import OfficeStaffDashBoard
        OfficeStaffDashBoard()
