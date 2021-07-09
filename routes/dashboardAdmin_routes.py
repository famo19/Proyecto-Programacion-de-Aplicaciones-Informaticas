from flask import render_template, request
import requests
from logic.categorias_logic import CategoriasLogic
from logic.admin_logic import AdminLogic


class DashboardAdminRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/categorias/create", methods=["GET", "POST"])
        def createCat():
            catLogic = CategoriasLogic()
            if request.method == "GET":
                allCategorias = catLogic.getAllCats()
                return render_template("categories.html", categorias=allCategorias)
            elif request.method == "POST":
                # Iniciando logica
                adminLogic = AdminLogic()
                # Form y datos de bd
                categoria = requests.form["cat"]
                idUsuario = int(adminLogic.getIdAdmin())
                # todo agregar ultimo param idusuario
                rows = catLogic.insertCat(categoria, idUsuario)
                allCategorias = catLogic.getAllCats()
                return render_template("categories.html", categorias=allCategorias)
                # TODO ESPERAR A QUE TRABAJEN LA VARIABLE SESIÓN A UTILIZAR PARA ADMIN Y MODIFICAR SENTENCIA SQL PARA ADMIN

        """@ app.route("/categorias/show")
        def showCat():
            HACER CODIGO EN DADO CASO NO SE PUEDA PROCESAR EN LA MISMA PAGINA LA CREACION Y DESPLIEGUE DE LAS CATEGORIAS
            return render_template("books.html")"""

        @ app.route("/categorias/delete", methods=["GET", "POST"])
        def deleteBooks():
            if request.method == "GET":
                return render_template("categoriesDelete.html")
            elif request.method == "POST":
                # Iniciar logica
                catLogic = CategoriasLogic()
                # Obtener datos del form
                idCat = requests.form["deleteCat"]
                # Mandando datos a database
                rows = catLogic.deleteCat(idCat)
                accion = "Eliminó"
                return render_template("done.html", accion=accion)
