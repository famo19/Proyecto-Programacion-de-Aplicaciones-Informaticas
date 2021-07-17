from flask import render_template, redirect, request, session
import requests
from logic.request_logic import RequestLogic

class RequestRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/request", methods=["GET", "POST"])
        def createReq():
            if session["userType"] == "cliente":
                ReqLogic = RequestLogic
                if request.method == "GET":
                    allRequests = ReqLogic()
                    return render_template("request.html")
                elif request.method == "POST":
                    logic = RequestLogic()
                    selectedName = request.form["name"]
                    selectedEmail = request.form["email"]
                    selectedBook = request.form["book"]
                    selectedYear = request.form["year"]
                    selectedAuthor = request.form["author"]
                    selectedMessage = request.form["message"]
                    rows = logic.insertRequest(selectedName,selectedEmail,selectedBook,selectedYear,selectedAuthor,selectedMessage)
                    return render_template("request.html")