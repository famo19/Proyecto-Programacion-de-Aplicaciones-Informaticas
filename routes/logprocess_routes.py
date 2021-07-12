from flask import render_template, request, redirect, session
from logic.user_logic import UserLogic
from logic.admin_logic import AdminLogic
import bcrypt


class LogProcessRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "GET":
                return render_template("login.html")
            elif request.method == "POST":
                logic = UserLogic()
                logicAdmin = AdminLogic()
                username = request.form["user"]
                password = request.form["password"]
                userDict = logic.getRowByUser(username)
                adminDict = logicAdmin.getRowByAdmin(username)

                # validar si userDict no es vacio
                if len(userDict) != 0:
                    # user existe
                    salt = userDict["salt"].encode("utf-8")
                    strPassword = password.encode("utf-8")
                    hashPassword = bcrypt.hashpw(strPassword, salt)
                    dbPassword = userDict["password"].encode("utf-8")
                    if hashPassword == dbPassword:
                        # se valido la password, se puede crear sesion y pasar al dashboard
                        session["userType"] = "cliente"
                        session["login_user"] = username
                        session["loggedIn"] = True
                        return redirect("/dashboard")
                    else:
                        return redirect("login")
                elif len(adminDict) != 0:
                    strPassword = password
                    dbPassword = adminDict["password"]
                    if password == dbPassword:
                        # se valido la password, se puede crear sesion y pasar al dashboard
                        session["userType"] = "admin"
                        session["login_admin"] = username
                        session["loggedIn"] = True
                        return redirect("/dashboard")
                    else:
                        return redirect("login")
                else:
                    # user no existe
                    return redirect("login")

                return redirect("login")
