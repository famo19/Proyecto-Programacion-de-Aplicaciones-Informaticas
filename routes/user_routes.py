from flask import render_template, request, session
from logic.admin_logic import AdminLogic
from logic.categorias_logic import CategoriasLogic
from logic.resumen_logic import ResumenLogic
from logic.user_logic import UserLogic
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
                return render_template("categoriesDelete.html")
            elif request.method == "POST":
                # Iniciar logica
                catLogic = CategoriasLogic()
                # Obtener datos del form
                idCat = int(request.form["deleteCat"])
                # Mandando datos a database
                rows = catLogic.deleteCat(idCat)
                accion = "eliminó"
                return render_template("done.html", accion=accion, rows=rows)
