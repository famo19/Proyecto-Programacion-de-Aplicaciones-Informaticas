from flask import render_template, request, session
import requests
from logic.categorias_logic import CategoriasLogic
from logic.admin_logic import AdminLogic


class CategoriasRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/categorias/create", methods=["GET", "POST"])
        def createCat():
            if session["userType"] == "admin":
                catLogic = CategoriasLogic()
                if request.method == "GET":
                    allCategorias = catLogic.getAllCats()
                    return render_template("categories.html", categorias=allCategorias)
                elif request.method == "POST":
                    # Iniciando logica
                    adminLogic = AdminLogic()
                    # Form y datos de bd
                    categoria = request.form["cat"]
                    adminDict = adminLogic.getRowByAdmin(
                        session["login_admin"])
                    idAdmin = adminDict["id"]
                    # todo agregar ultimo param idusuario
                    rows = catLogic.insertCat(categoria, idAdmin)
                    allCategorias = catLogic.getAllCats()
                    # TODO INTENTAR HACER UNA VISTA SQL
                    return render_template("categories.html", categorias=allCategorias)

        @ app.route("/categorias/delete", methods=["GET", "POST"])
        def deleteCat():
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
