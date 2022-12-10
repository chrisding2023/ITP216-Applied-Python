from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sl

app = Flask(__name__)
db = "favouriteFoods.db"
username = ""


# root end point
# routes to login unless client has already logged in
@app.route("/")
def home():
    """
    Checks whether the user is logged in and returns appropriately.
    
    :return: renders login.html if not logged in,
                redirects to client otherwise.
    """
    # TODO: your code goes here and replaces 'pass' below
    return render_template("login.html", message="Please login to continue")


# client endpoint
# renders appropriate template (admin or user)
@app.route("/client")
def client():
    """
    Renders appropriate template (admin or user)

    :return: redirects home if not logged in,
                renders admin.html if logged in as admin,
                user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    global username
    if username == "admin":
        return render_template("admin.html", username=username, message="Welcome back.", result=db_get_user_list())
    else:
        return render_template("user.html", username=username,fav_food=db_get_food(username))


# create user endpoint (admin only)
# adds new user to db, then re-renders admin template
@app.route("/action/createuser", methods=["POST", "GET"])
def create_user():
    """
    Callable from admin.html only
    Adds a new user to db by calling db_create_user, then re-renders admin template

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        un = request.form["username"]
        pw = request.form["password"]
        db_create_user(un,pw)
    return redirect(url_for("client"))


# remove user endpoint (admin only)
# removes user from db, then re-renders admin template
@app.route("/action/removeuser", methods=["POST", "GET"])
def remove_user():
    """
    Callable from admin.html only
    Removes user from the db by calling db_remove_user, then re-renders admin template.

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        un = request.form["username"]
        db_remove_user(un)
    return redirect(url_for("client"))

# set food endpoint (user only)
# updates user food, then re-renders user template
@app.route("/action/setfood", methods=["POST", "GET"])
def set_food():
    """
    Callable from user.html only,
    Updates user food by calling db_set_food, then re-renders user template

    :return: redirects to home if user not logged in,
                re-renders user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    global username
    if request.method == "POST":
        food = request.form["set_fav_food"]
        db_set_food(username, food)
    return redirect(url_for("client"))

# login endpoint
# allows client to log in (checks creds)
@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Allows client to log in
    Calls db_check_creds to see if supplied username and password are correct

    :return: redirects to client if login correct,
                redirects back to home otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    global username
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if db_check_creds(username,password):
            return redirect(url_for("client"))
    return redirect(url_for("home"))


# logout endpoint
@app.route("/logout", methods=["POST", "GET"])
def logout():
    """
    Logs client out, then routes to login
    Remove the user from the session
    :return: redirects back to home
    """
    # TODO: your code goes here and replaces 'pass' below
    global username
    username = ""
    return redirect(url_for("home"))


def db_get_user_list() -> dict:
    """
    Queries the DB's userfoods table to get a list
    of all the user and their corresponding favorite food for display on admin.html.
    Called to render admin.html template.

    :return: a dictionary with username as key and their favorite food as value
                this is what populates the 'result' variable in the admin.html template
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    curs2 = conn.cursor()
    stmt1 = "SELECT username FROM credentials;"
    data = curs.execute(stmt1)
    dic = {}

    for k in data:
        if k[0] == "admin":
            continue
        stmt2 = "SELECT food FROM userfoods WHERE username=?;"
        v = (str(k[0]),)
        value = curs2.execute(stmt2,v)
        for i in value:
            dic[k[0]] = i[0]
    return dic

def db_create_user(un: str, pw: str) -> None:
    """
    Add provided user and password to the credentials table
    Add provided user to the userfoods table
    and sets their favorite food to "not set yet".
    Called from create_user() view function.

    :param un: username to create
    :param pw: password to create
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un,pw)
    stmt = "INSERT INTO credentials (username, password) VALUES(?,?)"
    v2 = (un,)
    stmt2 = "INSERT INTO userfoods(username, food) VALUES (?,'None')"
    curs.execute(stmt,v)
    curs.execute(stmt2,v2)
    conn.commit()
    conn.close()


def db_remove_user(un: str) -> None:
    """
    Removes provided user from all DB tables.
    Called from remove_user() view function.

    :param un: username to remove from DB
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un,)
    stmt = "DELETE FROM credentials WHERE username = ?"
    curs.execute(stmt,v)
    conn.commit()
    conn.close()


def db_get_food(un: str) -> str:
    """
    Gets the provided user's favorite food from the DB.
    Called to render user.html fav_food template variable.

    :param un: username to get favorite food of
    :return: the favorite food of the provided user as a string
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un,)
    stmt = "SELECT FOOD FROM userfoods WHERE username = ?"
    data = curs.execute(stmt,v)
    for i in data:
        return i[0]



def db_set_food(un: str, ff: str) -> None:
    """
    Sets the favorite food of user, un param, to new incoming ff (favorite food) param.
    Called from set_food() view function.

    :param un: username to update favorite food of
    :param ff: user's new favorite food
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (ff,un)
    stmt = "UPDATE userfoods SET food = ? WHERE username = ?"
    curs.execute(stmt,v)
    conn.commit()
    conn.close()


def db_check_creds(un: str, pw: str) -> bool:
    """
    Checks to see if supplied username and password are in the DB's credentials table.
    Called from login() view function.

    :param un: username to check
    :param pw: password to check
    :return: True if both username and password are correct, False otherwise.
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un,)
    stmt = "SELECT password from credentials WHERE username = ?"
    data = curs.execute(stmt,v)
    for i in data:
        return i[0] == pw


if __name__ == "__main__":
    # Unit test of db_get_user_list()
    print(db_get_user_list())
    # TODO: Unit test your other db functions here

    # Start flask app
    app.secret_key = os.urandom(12)
    app.run(debug=True)
