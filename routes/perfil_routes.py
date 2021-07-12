from flask import render_template, redirect, request
import requests
from logic.perfil_logic import PerfilLogic


class PerfilRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/perfil", methods=["GET", "POST"])
        def perfil():
            if request.method == "GET":
                return render_template("perfil.html")
            elif request.method == "POST":
                logic = PerfilLogic()
                selectedNombre = request.form["nombre"]
                selectedEdad = request.form["edad"]
                selectedPais = request.form["pais"]
                result = logic.insertPerfil(selectedNombre, selectedEdad, selectedPais, "1")
                return selectedNombre #render_template("perfil.html")
