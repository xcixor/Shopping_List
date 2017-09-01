from flask import Flask, render_template, redirect, url_for, request

app = Flask (__name__)

@app.route('/')
def index():
    return render_template("sign_up.html")

@app.route('/login')
def login():
    return render_template("sign_in.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/sign_in', methods = ['POST'])
def sign_in():
    return redirect(url_for('dashboard'))

@app.route('/sign_up', methods = ['POST'])
def sign_up():
    return redirect(url_for('dashboard'))

class User(object):
    def __init__(self, first_name, last_name, email, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.password = password
        

class ShareShoppingList(object):
    def share_list(self, shopping_List):
        pass

class Shopping_List(object):
    def __init__(self, name, itemsList):
        self.name = name
        self.itemsList = itemsList

class Shopping_List_Item(object):
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Client(object):
    def create_account(self, user):
        pass
    def user_login(self, user):
        pass
    def track_shoppingList(self, shopping_List):
        pass
    def track_shoppingList_item(self, item):
        pass

class UserDAO(object):
    def save_user(user):
        pass
    def login_user(user):
        pass
    def delete_user(user):
        pass

class shoppingListDAO(object):
    def __init__(self):
        self.shopping_list = shopping_list
    def save_shoppingLists(shopping_List):
        pass
    def show_shoppinglists(lists):
        pass
    def edit_shoppinglist(shopping_List):
        pass
    def delete_shoppinglist(shopping_List):
        pass

class Shopping_List_ItemDAO(object):
    def __init__(self):
        self.item_list = item_list
    def save_item(item):
        pass
    def show_items(list):
        pass
    def edit_item(item):
        pass
    def delete_item(item):
        pass

if __name__=='__main__':
    app.run(debug = True, port = 8000,host='0.0.0.0')
