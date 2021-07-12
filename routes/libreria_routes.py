from flask import render_template, request, redirect, session
from logic.libreria_logic import LibreriaLogic
from logic.user_logic import UserLogic
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
            result = logic.getLibroByTitle(titulo)
            return render_template("books.html", result=result)

        @app.route("/libreria/deleteBooks")
        def deleteBooks():
            return "borrar libro"