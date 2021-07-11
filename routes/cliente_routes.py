from flask import render_template, redirect, request
import requests


class DashboardClientRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/dashboard_cliente")
        def dashboard():
            return render_template("dashboard_cliente.html")