from flask import Flask, render_template
from routes.main_routes import MainRoutes
from routes.libreria_routes import LibreriaRoutes
from routes.dashboard_routes import DashboardRoutes
from routes.busqueda_routes import BusquedaRoutes
from routes.highlights_routes import HighlightRoutes
from routes.logprocess_routes import LogProcessRoutes
from routes.register_routes import RegisterRoutes
from routes.perfil_routes import PerfilRoutes
from routes.categorias_routes import CategoriasRoutes
from routes.resumen_routes import ResumenRoutes
from routes.request_routes import RequestRoutes
from routes.password_routes import PasswordRoutes
from routes.card_routes import CardRoutes
from routes.user_routes import UserRoutes
import bcrypt

app = Flask(__name__)
app.secret_key = "1secret2key3!+"

MainRoutes.configure_routes(app)
LibreriaRoutes.configure_routes(app)
HighlightRoutes.configure_routes(app)
RegisterRoutes.configure_routes(app)
LogProcessRoutes.configure_routes(app)
DashboardRoutes.configure_routes(app)
BusquedaRoutes.configure_routes(app)
PerfilRoutes.configure_routes(app)
CategoriasRoutes.configure_routes(app)
ResumenRoutes.configure_routes(app)
RequestRoutes.configure_routes(app)
PasswordRoutes.configure_routes(app)
CardRoutes.configure_routes(app)
UserRoutes.configure_routes(app)

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


@app.route("/resumen")
def resumen():
    return render_template("resumen.html")


@app.route("/requestView")
def requestView():
    return render_template("manejosolicitudes.html")


@app.route("/modify")
def modify():
    return render_template("modify.html")


@app.route("/perfilAdmin")
def perfilAdmin():
    return render_template("perfilAdmin.html")


if __name__ == "__main__":
    app.run(debug=True)
