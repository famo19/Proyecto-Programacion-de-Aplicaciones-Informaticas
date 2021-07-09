from flask import Flask, render_template
from routes.libreria_routes import LibreriaRoutes
from routes.highlights_routes import HighlightRoutes
import bcrypt

app = Flask(__name__)
app.secret_key = "Bad1secret2key3!+"

LibreriaRoutes.configure_routes(app)
HighlightRoutes.configure_routes(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("registration.html")


@app.route("/dashboard_cliente")
def dashboardCliente():
    return render_template("dashboard_cliente.html")


@app.route("/dashboard_admin")
def dashboardAdmin():
    return render_template("dashboard_admin.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


@app.route("/resumen")
def resumen():
    return render_template("resumen.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/buscar")
def buscar():
    return render_template("busqueda.html")



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