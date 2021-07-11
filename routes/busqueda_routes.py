from flask import render_template, request, redirect, session

class BusquedaRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/busqueda", methods=["GET", "POST"])
        def searchByTitle():
            if request.method == "GET":
                return render_template("busqueda.html")
            elif request.method == "POST":
                selectedResumen = request.form["titulo"]
                session["titulo"] = selectedResumen
                return redirect("busqueda.html", selectedResumen=selectedResumen)
        
        def searchByCategory():
            if request.method == "GET":
                return render_template("busqueda.html")
            elif request.method == "POST":
                selectedResumen = request.form["titleCat"]
                session["titleCat"] = selectedResumen
                return redirect("busqueda.html", selectedResumen=selectedResumen)


