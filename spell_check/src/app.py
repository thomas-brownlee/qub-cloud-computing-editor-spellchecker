"""
 Flask Application 
===================

This module is designed to set up an api end point to run.

"""

import json

from flask import Flask, Response, request

from spell_check.src import spell_checker

app = Flask(__name__)


@app.route("/api/spell-check/service/ping", methods=["GET"])
def ping():
    """
    Runs the api call for a ping to check the service is active
    """
    reply: str = json.dumps({"status": "active"})
    r = Response(response=reply, status=200, mimetype="application/json")
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r


@app.route("/api/spell-check", methods=["GET"])
def spell_check_function():
    """
    Runs the api calls for the Spell Checker
    """
    response: dict[str, bool | str | int] = {"error": False, "string": "", "answer": 0}

    if not "text" in request.args:
        response["error"] = True
        response["string"] = "Missing parameters - must have an text"

    if "text" in request.args:
        text: str = str(request.args.get("text"))
        response: dict[str, bool | str | int] = spell_checker.spell_check(text)

    reply: str = json.dumps(response)
    r = Response(response=reply, status=200, mimetype="application/json")
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
