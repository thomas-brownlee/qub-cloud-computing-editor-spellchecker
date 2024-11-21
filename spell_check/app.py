"""
 Flask Application 
===================

This module is designed to setup an api end point to run.

This applications uses env variables to configure both,
the Host IP and Port Number.
- HOST_IP sets the host ip values (defaults to "0.0.0.0") 
- IMAGE_PORT_NUM sets the port number (defaults to "80")

"""

import json
import os

from flask import Flask, Response, request

from src import spell_checker

HOST_IP: str | None = os.getenv("HOST_IP")
PORT_NUM: str | None = os.getenv("IMAGE_PORT_NUM")

if HOST_IP is None:  # if their is no host ip default to "0.0.0.0"
    HOST_IP = "0.0.0.0"

if PORT_NUM is None:  # if their is no port number default to 80
    PORT_NUM = "80"

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
    app.run(host=HOST_IP, port=PORT_NUM)
