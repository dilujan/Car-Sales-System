from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

from currency_converter import CurrencyConverter
import datetime

from Controller.Seller import Seller
from POJO.Sale import Sale


class SaleView:

    # Create sale view UI
    def __init__(self, regNo, finalAmount):
        self.c = CurrencyConverter()

        self.window = Tk()
        self.window.title('Confirm to sale')
        self.window.geometry('350x300+200+250')

        self.lbl_regNo = Label(self.window, text='Car reg_no')
        self.fld_regNo = Entry(self.window)
        self.fld_regNo.insert(END, regNo)

        self.lbl_finalAmount = Label(self.window, text='Final amount')
        self.fld_finalAmount = Entry(self.window)
        self.fld_finalAmount.insert(END, finalAmount)

        self.lbl_selectCurrencyType = Label(self.window, text='Select Currency Type')
        self.combo_selectCurrencyType = Combobox(self.window, postcommand=self.selectCurrencyType)

        self.btn_confirm = Button(self.window, text='Confirm', command=self.confirm)

        self.lbl_regNo.grid(row=0, column=0, padx=8, pady=8)
        self.fld_regNo.grid(row=0, column=1, padx=8, pady=8)
        self.lbl_finalAmount.grid(row=1, column=0, padx=8, pady=8)
        self.fld_finalAmount.grid(row=1, column=1, padx=8, pady=8)
        self.lbl_selectCurrencyType.grid(row=2, column=0, padx=8, pady=8)
        self.combo_selectCurrencyType.grid(row=2, column=1, padx=8, pady=8)

        self.btn_confirm.grid(row=3, column=1, padx=8, pady=8)

        self.window.mainloop()

    def selectCurrencyType(self):
        self.combo_selectCurrencyType['values'] = list(self.c.currencies)

    def confirm(self):
        """This method convert final amount to customer selected currency type, if any exception-
        occurs, when convert currency. it caption the exception and sent message to user."""

        # call the sale method in controller class pass those sell information to it.
        regNo = self.fld_regNo.get()
        default_currency = self.fld_finalAmount.get()
        selectedCurrencyType = self.combo_selectCurrencyType.get()
        timeStamp = datetime.datetime.now()
        try:
            convertCurrency = self.c.convert(default_currency, 'GBP', selectedCurrencyType)
            sale = Sale(time_stamp=timeStamp, final_amount=default_currency, initial_currencyType=selectedCurrencyType,
                        initial_currency=convertCurrency, regNo=regNo)

            output = Seller().addNewSale(sale)

            if output:
                mb.showinfo('Message from system', 'successfully sold')
                self.window.destroy()
            else:
                mb.showwarning('Message from system', 'something wrong, please correct that')

        except:
            mb.showwarning('Message from system', 'RateNotFoundError, Please select another currency type')
