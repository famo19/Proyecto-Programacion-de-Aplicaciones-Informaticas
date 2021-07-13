from flask import render_template, request, redirect, session
from logic.busqueda_logic import BusquedaLogic

class BusquedaRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/buscar", methods=["GET", "POST"])
        def buscar():
            if request.method == "GET":
                return render_template("busqueda.html")
            elif request.method == "POST":
                logic = BusquedaLogic()
                selectedResumen = request.form["titulo"]
                result = logic.getResumenByTitle(selectedResumen)
                session["titulo"] = selectedResumen
                return render_template("busqueda.html", result=result)
        
        """def searchByCategory():
            if request.method == "GET":
                return render_template("busqueda.html")
            elif request.method == "POST":
                selectedResumen = request.form["titleCat"]
                session["titleCat"] = selectedResumen
                return redirect("busqueda.html", selectedResumen=selectedResumen)"""


