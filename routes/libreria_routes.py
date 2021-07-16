from flask import render_template, request, redirect, session
from logic.libreria_logic import LibreriaLogic
from logic.user_logic import UserLogic
from logic.resumen_logic import ResumenLogic
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
            return render_template("books.html", result=result)

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