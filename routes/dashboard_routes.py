from flask import render_template, redirect, request
import requests
from logic.user_logic import UserLogic


class DashboardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/dashboard")
        def dashboard():
            return render_template("dashboard.html")
        @app.route("/dashboard_cliente")
        def dashboard_cliente():
            return render_template("dashboard_cliente.html")   