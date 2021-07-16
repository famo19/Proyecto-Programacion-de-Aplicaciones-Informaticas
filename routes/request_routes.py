from flask import render_template, redirect, request, session
import requests
from logic.request_logic import RequestLogic

class RequestRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/request")