class UserDAO(object):
    def __init__(self):
        self.myList = []
    def getlist (self):
        return self.myList
    def setlist(self, list):
        self.userList = list
    # def save_user():
    #     pass
    # def login_user(user):
    #     pass
    # def delete_user(user):
    #     pass

# if __name__ == '__main__':
#     UserDAO = myDAO()
#     user1 = User("Alice", "Njambi", "alice@email.com", "alie", "1234")
#     user2 = User("James", "Matumbi", "matus@email.com", "matus", "0987")
#     userList.add(user1)
#     userList.add(user2)