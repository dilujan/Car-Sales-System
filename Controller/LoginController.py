from Model.LoginDao import LoginDAO


class LoginController:

    """LoginController class is a controller class. it manages login authentication that are made by user.
    It is an intermediate class between Login Ui and Login Dao. When load the Login UI by system, The user-name
     and password are given by user then the authentication method in this class called by the system to find-
     the valid user. the function calls the LoginDAO model class's (backed end class)-
      getUserInfo() function. it fetch the-
     information from database and give to  authentication method."""

    # Create the constructor function.
    # Create the LoginDAO() object for model class.
    def __init__(self):
        self.__loginDao = LoginDAO()

    """The function get the user object as argument when user click the submit button on login UI.
    The object LoginDAO call the function getUserInfo() that define in the class. it returns all the user-
    information in database."""
    def authentication(self, user):
        userInfo = self.__loginDao.getUserInfo()

        for row in userInfo:
            # Check the username and password, which are given by user .
            # If the user name and passwords correct, it'll return the roll according the user.
            if user.getUserName() == row[0] and user.getPassword() == row[1]:
                return row[2]






