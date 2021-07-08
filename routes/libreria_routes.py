from flask import render_template, request, redirect
from logic.libreria_logic import LibreriaLogic
import requests

class LibreriaRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/libreria")
        def libreria():
            logic = LibreriaLogic()
            userId = "1"
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
