import json
import azure.functions as func
import logging

import db

app = func.FunctionApp()

@app.function_name(name="GetGames")
@app.route(route="games", auth_level=func.AuthLevel.ANONYMOUS)
def get_games(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(db.get_games()),
        mimetype="application/json"
    )

@app.function_name(name="GetGroups")
@app.route(route="groups", auth_level=func.AuthLevel.ANONYMOUS)
def get_groups(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(db.get_groups()),
        mimetype="application/json"
    )

@app.function_name(name="GetLinkTypes")
@app.route(route="linkTypes", auth_level=func.AuthLevel.ANONYMOUS)
def get_link_types(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(db.get_link_types()),
        mimetype="application/json"
    )

@app.function_name(name="GetPlayers")
@app.route(route="players", auth_level=func.AuthLevel.ANONYMOUS)
def get_players(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(db.get_players()),
        mimetype="application/json"
    )

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )
