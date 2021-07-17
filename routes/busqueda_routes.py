from flask import render_template, request, redirect, session
from logic.busqueda_logic import BusquedaLogic

class BusquedaRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/buscar", methods=["GET", "POST"])
        def buscar():
            if request.method == "GET":
                logic = BusquedaLogic()
                categorias =logic.getAllCats()
                return render_template("busqueda.html", categorias=categorias)
            elif request.method == "POST":
                logic = BusquedaLogic()
                selectedResumen = request.form["titulo"]
                result = logic.getResumenByTitle(selectedResumen)
                session["titulo"] = selectedResumen
                return render_template("busqueda.html", result=result)

        @app.route("/buscarByCat", methods=["GET", "POST"])
        def buscarByCat():
            if request.method == "GET":
                return render_template("busqueda.html")
            elif request.method == "POST":
                idCat = int(request.form["cat"])
                logic = BusquedaLogic()
                result = logic.getResumenByCategory(idCat)
                return render_template("busqueda.html", result=result)





            

        


