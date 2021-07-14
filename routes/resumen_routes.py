from flask import render_template, request, session
from logic.admin_logic import AdminLogic
from logic.categorias_logic import CategoriasLogic
from logic.resumen_logic import ResumenLogic
import requests


class ResumenRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/resumen/create", methods=["GET", "POST"])
        def createRes():
            if session["userType"] == "admin":
                resLogic = ResumenLogic()
                catLogic = CategoriasLogic()
                if request.method == "GET":
                    allCategorias = catLogic.getAllCats()
                    allResumes = resLogic.getAllResumes()
                    return render_template("resumen.html", resumenes=allResumes, categorias=allCategorias)
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

        @ app.route("/resumen/delete", methods=["GET", "POST"])
        def deleteRes():
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

        @ app.route("/resumen/update", methods=["GET", "POST"])
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
                idCat = request.form["cat"]
                idRes = int(request.form["idResu"])
                # Mandando datos a database
                rows = resLogic.updateRes(
                    titulo, sinopsis, recomendacion, infoAutor, contenido, idAdmin, idCat, idRes)
                accion = "actualizó"
                return render_template("done.html", accion=accion, rows=rows)
