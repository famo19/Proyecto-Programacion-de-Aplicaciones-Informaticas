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
                    return render_template("usuarios.html", users=allUsers)
'''
                elif request.method == "POST":
                    # Iniciando logica
                    adminLogic = AdminLogic()
                    # Form y datos de bd
                    titulo = request.form["title"]
                    sinopsis = request.form["sinop"]
                    recomendacion = request.form["recom"]
                    infoAutor = request.form["infAutor"]
                    contenido = request.form["content"]
                    adminDict = adminLogic.getRowByAdmin(
                        session["login_admin"])
                    idAdmin = adminDict["id"]
                    idCat = request.form["cat"]
                    # Mandar datos
                    rows = resLogic.insertRes(
                        titulo, sinopsis, recomendacion, infoAutor, contenido, idAdmin, idCat)
                    allResumes = resLogic.getAllResumes()
                    allCategorias = catLogic.getAllCats()
                    return render_template("resumen.html", resumenes=allResumes, categorias=allCategorias)
'''
'''
        @ app.route("/user/delete", methods=["GET", "POST"])
        def deleteUser():
            if request.method == "GET":
                return render_template("resumenDelete.html")
            elif request.method == "POST":
                # Iniciar logica
                resLogic = ResumenLogic()
                # Obtener datos del form
                idRes = int(request.form["deleteRes"])
                # Mandando datos a database
                rows = resLogic.deleteResu(idRes)
                accion = "eliminó"
                return render_template("done.html", accion=accion, rows=rows)

        @ app.route("/user/update", methods=["GET", "POST"])
        def updateRes():
            if request.method == "GET":
                resLogic = ResumenLogic()
                catLogic = CategoriasLogic()
                resumen = resLogic.getResumenById(request.args["idRes"])
                allCategorias = catLogic.getAllCats()
                return render_template("resumenUpdate.html", resumen=resumen, categorias=allCategorias)
            elif request.method == "POST":
                # Iniciar logica
                resLogic = ResumenLogic()
                adminLogic = AdminLogic()
                # Obtener datos del form
                titulo = request.form["title"]
                sinopsis = request.form["sinop"]
                recomendacion = request.form["recom"]
                infoAutor = request.form["infAutor"]
                contenido = request.form["content"]
                adminDict = adminLogic.getRowByAdmin(
                    session["login_admin"])
                idAdmin = adminDict["id"]
                idCat = int(request.form["cat"])
                idRes = int(request.form["idResu"])
                # Mandando datos a database
                rows = resLogic.updateRes(
                    titulo, sinopsis, recomendacion, infoAutor, contenido, idAdmin, idCat, idRes)
                accion = "actualizó"
                return render_template("done.html", accion=accion, rows=rows)

        @ app.route("/user/ver", methods=["GET", "POST"])
        def verRes():
            if request.method == "GET":
                # Iniciar logica
                resLogic = ResumenLogic()
                resumen = resLogic.getResumenById(request.args["idRes"])
                return render_template("verResumen.html", resumen=resumen)
'''