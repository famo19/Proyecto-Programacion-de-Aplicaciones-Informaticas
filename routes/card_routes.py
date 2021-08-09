from flask import render_template, redirect, request, session
import requests
from logic.user_logic import UserLogic
import bcrypt

class CardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/cardConfirm", methods=["GET", "POST"])
        def cardConfirm():
            if request.method == "GET":
                return render_template("card.html")
            elif request.method == "POST":
                name = request.form["name"]
                number = request.form["card"]
                date = request.form["expDate"]
                code = request.form["cod"]

                restapi     = "https://credit-card-auth-api-cerberus.herokuapp.com"
                endpoint    = "/verify"

                url = f"{restapi}{endpoint}"

                data = {
                    "name": name,
                    "number": number,
                    "date": date,
                    "code": code,
                    "balance": 29.99 # el valor de la transaccion
                }

                response = requests.post(url, data=data)
                print(response)
                if response.status_code == 200:
                    dataJson = response.json()
                    if dataJson['response'] == '00':
                        print(dataJson)
                        session["userAccount"] = "premium"
                        return redirect("/dashboard_cliente")
                    else:
                        print(dataJson)
                        return redirect("/cardConfirm")
                else:
                    return redirect("/cardConfirm")