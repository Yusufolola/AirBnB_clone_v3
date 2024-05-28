#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    """return status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stat():
    """returns the statisticsof all objects"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("User")})
