"""
 Flask Application 
===================

This module is designed to setup an api end point to run.

"""

import json

from flask import Flask, Response, request
from src import spell_checker


app = Flask(__name__)


@app.route("/")
def adder():
    """
    Runs the api calls for the Spell Checker
    """
    response = {"error": False, "string": "", "answer": 0}

    if not "text" in request.args:
        response["error"] = True
        response["string"] = "Missing parameters - must have an text"

    if "text" in request.args:
        text = request.args.get("text")
        mistake_count, message_content = spell_checker.spell_check(text)

        # any issue in spell_check will return mistake_count to -1
        if mistake_count <= 0:
            response["answer"] = int(mistake_count)
            response["string"] = message_content
        if mistake_count == -1:
            response["error"] = True
            response["string"] = "Missing parameters - Text is not a string"
        if mistake_count == -2:
            response["error"] = True
            response["string"] = "Empty parameters - Text is not a string"

    reply = json.dumps(response)
    r = Response(response=reply, status=200, mimetype="application/json")
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
