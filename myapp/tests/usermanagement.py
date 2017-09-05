from myapp.user import User
from myapp.userDAO import UserDAO

import unittest

if __name__ == '__main__':
    myDAO = UserDAO()
    user1 = User("Alice", "Njambi", "alice@email.com", "alie", "1234")
    user2 = User("James", "Matumbi", "matus@email.com", "matus", "0987")
