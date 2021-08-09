from flask import render_template, request, redirect, session
from logic.libreria_logic import LibreriaLogic
from logic.user_logic import UserLogic
from logic.resumen_logic import ResumenLogic
from logic.categorias_logic import CategoriasLogic
import requests

class LibreriaRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/libreria")
        def libreria():
            logic = LibreriaLogic()
            logicUser = UserLogic()
            username = session['login_user']
            user = logicUser.getRowByUser(username)
            userId = user["id"]
            result = logic.getLibroByUserId(userId)
            """result = libros.values()"""
            return render_template("libreria.html", result=result)

        @app.route("/libreria/books/<string:titulo>")
        def books(titulo):
            logic = LibreriaLogic()
            session["viewingBook"] = titulo
            result = logic.getLibroByTitle(titulo)
            idCat = result["idCategoria"]
            #Sacando categoría
            logicCate = CategoriasLogic()
            categoria = logicCate.getCatById(idCat)
            if session["userAccount"] == "gratis":
                return render_template("booksFree.html", result=result, categoria=categoria)
            elif session["userAccount"] == "premium":
                #link para pdf y audio
                urlpdf = f"https://esen-restapi.herokuapp.com/pdf/{titulo}"
                urlaudio = f"https://esen-restapi.herokuapp.com/audio/{titulo}"
                responsepdf = requests.get(urlpdf)
                responseaudio = requests.get(urlaudio)
                if responsepdf.status_code == 200 & responseaudio.status_code == 200:
                    dataJsonPdf = responsepdf.json()
                    linkpdf = dataJsonPdf["archivo"]

                    dataJsonAudio = responseaudio.json()
                    linkaudio = dataJsonAudio["archivo"]

                    return render_template("booksPaid.html", result=result, categoria=categoria, linkpdf=linkpdf, linkaudio=linkaudio)
                else:
                    return render_template("booksPaid.html", result=result, categoria=categoria)

        @app.route("/libreria/books/addedBook")
        def addBook():
            #sacar datos del current viewing book
            titulo = session["viewingBook"]
            logicResumen = ResumenLogic()
            resumen = logicResumen.getResumenByTitle(titulo)
            idResumen = resumen["id"]
            sinopsis = resumen["sinopsis"]
            recomendacion = resumen["recomendación"]
            informacionDelAutor = resumen["informacionDelAutor"]
            contenido = resumen["contenido"]
            idCategoria = resumen["idCategoria"]
            #sacar id del usuario
            logicUser = UserLogic()
            username = session['login_user']
            user = logicUser.getRowByUser(username)
            userId = user["id"]
            #insertar el libro en la bd
            logicBook = LibreriaLogic()
            rows = logicBook.insertBook(titulo,sinopsis,recomendacion,informacionDelAutor,contenido,userId,idCategoria,idResumen)
            return redirect("/libreria")

        @app.route("/libreria/deleteBooks/<string:titulo>")
        def deleteBooks(titulo):
            logicUser = UserLogic()
            username = session['login_user']
            user = logicUser.getRowByUser(username)
            userId = user["id"]
            logicBook = LibreriaLogic()
            rows = logicBook.deleteBookByTitle(titulo, userId)
            return redirect("/libreria")

        """API ROUTES"""
        @app.route("/libreria/books/pdf")
        def pdfBook():
            #sacar datos del current viewing book
            titulo = session["viewingBook"]
            url = f"https://esen-restapi.herokuapp.com/audio/{titulo}"
            response = requests.get(url)
            if response.status_code == 200:
                dataJson = response.json()
                return render_template("places.html", id=id, place=dataJson)
            else:
                return redirect("/dashboard")
