from server import app
from flask import request
from server.service import rocket_service


@app.post("/rocket")
def post_rocket():
    rocket = request.get_json()
    error = rocket_service.create_rocket(rocket)
    if error is not None:
        return error, 400
    return rocket, 201


@app.get("/rocket")
def list_rocket():
    rockets = rocket_service.get_rockets()
    return rockets


@app.put("/rocket/<int:id>")
def update_rocket(id):
    rocket = request.get_json()
    error = rocket_service.update_rocket(id, rocket)
    if error is not None:
        return error, 400
    return rocket, 201
