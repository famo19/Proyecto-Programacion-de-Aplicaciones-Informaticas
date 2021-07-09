from flask import render_template, request, redirect
from logic.highlights_logic import HighlightsLogic

class HighlightRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/highlights/<string:titulo>/<string:copiedText>")
        def highlightsSaved(titulo, copiedText):
            logic = HighlightsLogic()
            userId = "1"
            rows = logic.insertHighlight(titulo, copiedText, userId)
            return render_template("saveHighlight.html", result=rows)