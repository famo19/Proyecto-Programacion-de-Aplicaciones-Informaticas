from flask import render_template, redirect, request, session
import requests
from logic.perfil_logic import PerfilLogic
from logic.user_logic import UserLogic


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
                logicUser = UserLogic()
                username = session['login_user']
                user = logicUser.getRowByUser(username)
                userId = user["id"]
                result = logic.insertPerfil(selectedNombre, selectedEdad, selectedPais, userId)
                return render_template("perfil.html")
