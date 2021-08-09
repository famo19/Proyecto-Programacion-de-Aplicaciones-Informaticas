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
                logic = PerfilLogic()
                logicUser = UserLogic()
                username = session['login_user']
                user = logicUser.getRowByUser(username)
                iduser = user["id"]
                perfil = logic.getPerfil(iduser)
                if len(perfil) > 0:
                    result = perfil[0]
                    return render_template("perfil.html",result=result)
                else:
                    result = []
                    return render_template("perfil.html",result=result)

            elif request.method == "POST":
                logic = PerfilLogic()
                selectedNombre = request.form["nombre"]
                selectedEdad = request.form["edad"]
                selectedPais = request.form["pais"]
                logicUser = UserLogic()
                username = session['login_user']
                user = logicUser.getRowByUser(username)
                userId = user["id"]
                perfil = logic.getPerfil(userId)
                if len(perfil) > 0:
                    result = logic.updatePerfil(selectedNombre, selectedEdad, selectedPais, userId)
                else:
                    result = logic.insertPerfil(selectedNombre, selectedEdad, selectedPais, userId)
                return redirect("/perfil")
