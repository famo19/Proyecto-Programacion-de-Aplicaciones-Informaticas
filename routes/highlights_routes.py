from flask import render_template, request, redirect, session
from logic.highlights_logic import HighlightsLogic

class HighlightRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/highlights")
        def highlights():
            logic = HighlightsLogic()
            userId = "1"
            result = logic.getAllHighlightsByUserId(userId)
            """result = libros.values()"""
            return render_template("highlights.html", result=result)

        @app.route("/highlights/<string:titulo>/<string:copiedText>")
        def highlightsSaved(titulo, copiedText):
            logic = HighlightsLogic()
            userId = "1"
            text = logic.getHighlightByUserId(userId)
            for element in text:
                if element["texto"] == copiedText:
                    return "ya se guardó este texto"
                #rows = logic.insertHighlight(titulo, copiedText, userId)
            session["tituloLibroH"] = titulo
            session["highlight"] = copiedText
            return redirect("/highlights/confirmation")

        @app.route("/highlights/confirmation", methods=["GET", "POST"])
        def highlightConfirm():
            if request.method == "GET":
                titulo = session.get("tituloLibroH")
                copiedText = session.get("highlight")
                return render_template("highlightConfirm.html", titulo=titulo, copiedText=copiedText)
            elif request.method == "POST":
                notas = request.form["notas"]
                if notas != "":
                    logic = HighlightsLogic()
                    titulo = session.get("tituloLibroH")
                    copiedText = session.get("highlight")
                    userId = "1"
                    rows = logic.insertHighlight(titulo, copiedText, notas, userId)
                    return redirect("/highlights")
                else:
                    return "Llenar el espacio de Notas"
        
        
        @app.route("/highlights/Delete/<string:txt>")
        def highlightDelete(txt):
            userId = "1"
            logic = HighlightsLogic()
            text = logic.deleteHighlightByText(txt,userId)
            return redirect("/highlights")
