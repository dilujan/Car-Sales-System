from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

from Controller.OfficeStaff import OfficeStaff


class SearchCar:

    # Create search car UI
    def __init__(self):
        self.window = Tk()
        self.window.title('Search car')
        self.window.geometry('350x200+500+250')

        self.lbl_selectModel = Label(self.window, text='Select model')
        self.combo_selectModel = Combobox(self.window, postcommand=self.getModelName)
        self.lbl_selectManufacture = Label(self.window, text='Select manufacture')
        self.combo_selectManufacture = Combobox(self.window, postcommand=self.getManufactureName)

        self.btn_clear = Button(self.window, text='Clear', command=self.clear)
        self.btn_search = Button(self.window, text='Search', command=self.search)
        self.btn_back = Button(self.window, text='Back', command=self.back)

        self.lbl_selectModel.grid(row=1, column=1, padx=8, pady=16)
        self.lbl_selectManufacture.grid(row=2, column=1, padx=8, pady=16)
        self.combo_selectModel.grid(row=1, column=2, padx=8, pady=16)
        self.combo_selectManufacture.grid(row=2, column=2, padx=8, pady=16)
        self.btn_back.place(x=32, y=150)
        self.btn_search.place(x=150, y=150)
        self.btn_clear.place(x=255, y=150)

        self.window.mainloop()

    def getModelName(self):
        self.combo_selectModel['values'] = OfficeStaff().getModelName()

    def getManufactureName(self):
        self.combo_selectManufacture['values'] = OfficeStaff().getManufactureName()

    def clear(self):
        self.combo_selectModel.delete(0, 'end')
        self.combo_selectManufacture.delete(0, 'end')

    def search(self):
        """Get the values (Manufacture name , model name) that are selected by user. pass those values-
          to Office staff class search method. that method contact the DAO class and get the details-
          (Car details) under the user selection that are model name, manufacture name or model and
           manufacture name. the result will be a list."""

        if self.combo_selectManufacture.get() == '' and self.combo_selectModel.get() == '':
            mb.showwarning('Message from system', 'Select at least  one model or manufacture')

        else:
            # call the controller class method and get the result as list.
            searchList = OfficeStaff().searchCar(self.combo_selectModel.get(), self.combo_selectManufacture.get())

            # Create a temporary window to show the result as table
            tempWindow = Tk()
            tempWindow.title("Search Result")

            # code for creating table
            # find total number of rows and columns in list
            for i in range(len(searchList)):
                for j in range(len(searchList[0])):
                    tempEntry = Entry(tempWindow, width=20, fg='blue',
                                      font=('Arial', 16, 'bold'))
                    tempEntry.grid(row=i, column=j)
                    tempEntry.insert(END, searchList[i][j])
            tempWindow.mainloop()

    def back(self):
        self.window.destroy()
        from UI.OfficeStaffDashboard import OfficeStaffDashBoard
        OfficeStaffDashBoard()
