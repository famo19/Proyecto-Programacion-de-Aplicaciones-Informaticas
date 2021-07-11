from flask import Flask, render_template
from routes.libreria_routes import LibreriaRoutes
from routes.dashboard_routes import DashboardRoutes
from routes.busqueda_routes import BusquedaRoutes
from routes.highlights_routes import HighlightRoutes
from routes.logprocess_routes import LogProcessRoutes
from routes.register_routes import RegisterRoutes
import bcrypt

app = Flask(__name__)
app.secret_key = "1secret2key3!+"

LibreriaRoutes.configure_routes(app)
HighlightRoutes.configure_routes(app)
RegisterRoutes.configure_routes(app)
LogProcessRoutes.configure_routes(app)
DashboardRoutes.configure_routes(app)
BusquedaRoutes.configure_routes(app)

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/dashboard_admin")
def dashboardAdmin():
    return render_template("dashboard_admin.html")



@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


@app.route("/resumen")
def resumen():
    return render_template("resumen.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")





@app.route("/request")
def request():
    return render_template("request.html")


@app.route("/requestView")
def requestView():
    return render_template("manejosolicitudes.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/modify")
def modify():
    return render_template("modify.html")
    
@app.route("/perfilAdmin")
def perfilAdmin():
    return render_template("perfilAdmin.html")

if __name__ == "__main__":
    app.run(debug=True)