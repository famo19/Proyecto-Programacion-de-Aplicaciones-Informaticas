from flask import render_template, request, session
from logic.admin_logic import AdminLogic
from logic.categorias_logic import CategoriasLogic
from logic.resumen_logic import ResumenLogic
from logic.user_logic import UserLogic
import bcrypt
import requests

class UserRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/usuario/create", methods=["GET", "POST"])
        def createUser():
            if session["userType"] == "admin":
                userLogic = UserLogic()
                if request.method == "GET":
                    allUsers = userLogic.getAllUsers()
                    return render_template("usuarios.html", usuarios=allUsers)
                elif request.method == "POST":
                    # Iniciando logica
                    adminLogic = AdminLogic()
                    # Form y datos de bd
                    user = request.form["us"]
                    adminDict = adminLogic.getRowByAdmin(
                        session["login_admin"])
                    idAdmin = adminDict["id"]
                    # todo agregar ultimo param idusuario
                    rows = userLogic.insertCat(user, idAdmin)
                    allCategorias = userLogic.getAllUsers()
                    return render_template("usuarios.html", usuarios=allCategorias)
    
        @ app.route("/usuario/delete", methods=["GET", "POST"])
        def deleteUser():
            if request.method == "GET":
                return render_template("usuarioDelete.html")
            elif request.method == "POST":
                # Iniciar logica
                userLogic = UserLogic()
                # Obtener datos del form
                idUser = int(request.form["deleteUser"])
                # Mandando datos a database
                rows = userLogic.deleteUser(idUser)
                accion = "eliminó"
                return render_template("done.html", accion=accion, rows=rows)

        @ app.route("/usuario/update", methods=["GET", "POST"])
        def updateUser():
            if request.method == "GET":
                return render_template("usuarioUpdate.html")
            elif request.method == "POST":
                # Iniciar logica
                userLogic = UserLogic()
                # Obtener datos del form
                idUser = int(request.form["updateUser"])
                contraUser = request.form["contra"]

                salt = bcrypt.gensalt(rounds=14)
                strSalt = salt.decode("utf-8")
                encPassword = contraUser.encode("utf-8")
                hashPassword = bcrypt.hashpw(encPassword, salt)
                strPassword = hashPassword.decode("utf-8")
                # Mandando datos a database
                rows = userLogic.updatePassword(strPassword,strSalt, idUser)
                accion = "modifico"
                return render_template("done.html", accion=accion, rows=rows)
