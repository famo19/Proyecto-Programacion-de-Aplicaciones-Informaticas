from flask import render_template, redirect, request
import requests
from logic.user_logic import UserLogic


class DashboardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/dashboard")
        def dashboard():
            usuario = "cliente"
            if usuario == "cliente":
                return redirect("/dashboard_cliente")
            elif usuario == "admin":
                return redirect("/dashboard_admin")
        @app.route("/dashboard_cliente")
        def dashboard_cliente():
            return render_template("dashboard_cliente.html") 
        @app.route("/dashboard_admin")
        def dashboard_admin():
            return render_template("dashboard_admin.html")    