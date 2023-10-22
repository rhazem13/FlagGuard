from flask import Blueprint, request, jsonify, Response

service_bp = Blueprint("service", __name__)


@service_bp.get("/home")
def getHome():
    return {
        "hello": "world",
    }
