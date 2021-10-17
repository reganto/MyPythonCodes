class User:
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username.lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
