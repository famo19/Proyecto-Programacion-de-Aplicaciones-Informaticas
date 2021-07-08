from flask import render_template, request, redirect, session
from logic.libreria_logic import LibreriaLogic

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

        @app.route("/libreria/books")
        def books():
            titulo = request.query_string
            return titulo

        @app.route("/libreria/deleteBooks")
        def deleteBooks():
            return "borrar libro"
