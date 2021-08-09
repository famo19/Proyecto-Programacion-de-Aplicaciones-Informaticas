from flask import render_template, redirect, request, session
import requests
from logic.user_logic import UserLogic
import bcrypt

class PasswordRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/password", methods=["GET", "POST"])
        def password():
            if request.method == "GET":
                return render_template("password.html")

            elif request.method == "POST":
                logic = UserLogic()
                username = session["login_user"]
                Apassword = request.form["Apassword"]
                Npassword = request.form["Npassword"]
                Cpassword = request.form["Cpassword"]
                userDict = logic.getRowByUser(username)

                # validar si userDict no es vacio
                if len(userDict) != 0:
                    # user existe
                    salt = userDict["salt"].encode("utf-8")
                    strPassword = Apassword.encode("utf-8")
                    hashPassword = bcrypt.hashpw(strPassword, salt)
                    dbPassword = userDict["password"].encode("utf-8")
                    if hashPassword == dbPassword:
                        if Npassword == Cpassword:
                            strSalt = salt.decode("utf-8")
                            encPassword = Npassword.encode("utf-8")
                            hashPassword = bcrypt.hashpw(encPassword, salt)
                            strPassword = hashPassword.decode("utf-8")
                            id = userDict["id"]
                            rows = logic.updatePassword(strPassword, strSalt, id)
                            return redirect("/login")
                        else:
                            return redirect("/password")
                    else: 
                        return redirect("/password")
