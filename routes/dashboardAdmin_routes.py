from flask import render_template
from logic.categorias_logic import CategoriasLogic


class LibreriaRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/categorias/create")
        def createCat():
            logic = CategoriasLogic()
            # TODO FALTA OBTENER LAS REPSUESTAS DEL FORMULARIO Y HACER CODIGO PARA LLAMAR AL INSERT CON SUS PARAMS
            """result = libros.values()"""
            return render_template("libreria.html")  # , result=result

# TODO HACER PAGINA PARA MOSTRAR
        @ app.route("/libreria/books")
        def books():
            return render_template("books.html")

# TODO HACER PAGINA PARA ELIMINAR CAT
        @ app.route("/libreria/deleteBooks")
        def deleteBooks():
            return "borrar libro"
