from flask import render_template
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
            return render_template("books.html")

        @app.route("/libreria/deleteBooks")
        def deleteBooks():
            return "borrar libro"
