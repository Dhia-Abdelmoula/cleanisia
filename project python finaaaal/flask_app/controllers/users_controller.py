from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.users_model import User
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

# ? ========== LOGIN PAGE ==========


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("registration.html")

# * ========== REGISTER method --- ACTION


@app.route("/users/register", methods=["post"])
def user_register():
    print(request.form)
    if not User.validate(request.form):
        return redirect("/register")

    # hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': pw_hash
    }
    # Save the user in DB
    user_id = User.create_user(data)
    # store the user_id in session
    session["user_id"] = user_id
    return redirect("/register")

# * =============== LOGIN =============


@app.route("/users/login", methods=["POST"])
def logins():

    # TODO Validate the user's email and password (Both are required !)

    data = {
        "email": request.form["email"]
    }

    user_in_db = User.get_user_by_email(data)
    # if email not found
    if not user_in_db:
        flash("invalid credentials", "log")
        return redirect("/logreg")

    # check password hash
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid credentials", "log")
        return redirect("/logreg")

    # All Good up to here
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

# ---------- dashboard- view

# # ? ========== Dashboard PAGE ==========


# @app.route("/dashboard")
# def dash():

#     #! route guard
#     if 'user_id' not in session:
#         return redirect("/logreg")

#     data = {
#         "id":  session["user_id"]
#     }
#     logged_user = User.get_by_id(data)

#     return render_template("dashboard.html", user=logged_user)

# # ------------ LOGOUT --------------


# @app.route("/logout")
# def logout():

#     # clear the session
#     session.clear()
#     return redirect("/logreg")