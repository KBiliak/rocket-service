from server import mysql
from server.db import rocket_repository


def create_rocket(rocket):
    print("create a rocket:", rocket)
    all_rockets = rocket_repository.get_rocket(mysql)
    name = rocket['name']
    for exist_rocket in all_rockets:
        exist_name = exist_rocket['name']
        if exist_name == name:
            return {"error": "rocket with this name already exists"}

    rocket_repository.create_rocket(mysql, rocket)
    return None


def update_rocket(id, rocket):
    print("rocket updated by id: id =", id, "rocket =", rocket)
    all_rockets = rocket_repository.get_rocket(mysql)
    new_name = rocket["name"]
    for ex_rocket in all_rockets:
        ex_name = ex_rocket["name"]
        ex_id = ex_rocket["id"]
        if ex_name == new_name and id != ex_id:
            return {"error": "rocket with this name already exists"}

    rocket_repository.update_rocket_id(mysql, rocket, id)
    return None


def get_rockets():
    return rocket_repository.get_rocket(mysql)
