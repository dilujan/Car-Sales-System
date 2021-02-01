from tkinter import messagebox as mb
from tkinter import *

from Controller.LoginController import LoginController
from POJO.User import User
from UI.OfficeStaffDashboard import OfficeStaffDashBoard
from UI.SellerDashboard import SellerDashboard


class LoginView:

    # Create a login user interface
    def __init__(self):

        self.window = Tk()
        self.window.title('Login')
        self.window.geometry('300x200+500+250')

        self.lbl_userName = Label(self.window, text='User Name')
        self.lbl_password = Label(self.window, text='Password')

        self.fld_userName = Entry()
        self.fld_password = Entry()

        btn_submit = Button(self.window, text='Submit',
                            command=self.submit)

        self.lbl_userName.place(x=16, y=48)
        self.lbl_password.place(x=16, y=96)

        self.fld_userName.place(x=96, y=48)
        self.fld_password.place(x=96, y=96)

        btn_submit.place(x=125, y=144)

        self.window.mainloop()

    """When user click the submit button the function will be called. the user name and password-
    are fetched from the entries.user object is created and set those values into user object.
    the authentication function in LoginController class is called and pass the created user object 
     as parameter (OOPS encapsulation). all the control and logic part is handled by the controller 
     class. the authentication method find who are the user office-staff or seller. if both are not-
      it won't be given the access to the system."""

    def submit(self):

        # Create the user object and set the values to the object.
        user = User()
        user.setUserName(self.fld_userName.get())
        user.setPassword(self.fld_password.get())

        # Pass the user object as argument to authentication function
        # The returns value store in result variable
        result = LoginController().authentication(user)

        # Give the access to the type of user
        if result == 'office-staff':
            # Print success message on window
            mb.showinfo('Message from system', 'Login Successfully by office staff ')
            # Destroy LoginUI
            self.window.destroy()
            # Open office staff dashboard
            OfficeStaffDashBoard()

        elif result == 'seller':
            # Print success message on window
            mb.showinfo('Message from system', 'Login Successfully by seller ')
            # Destroy LoginUI
            self.window.destroy()
            # Open seller dashboard
            SellerDashboard()

        else:
            # Print un-success message on window
            mb.showwarning('Message from system', 'The user name or password was wrong')
            # Clear the value on entries
            self.fld_userName.delete(0, 'end')
            self.fld_password.delete(0, 'end')


# This the main Method to run the programme:
if __name__ == '__main__':

    LoginView()
