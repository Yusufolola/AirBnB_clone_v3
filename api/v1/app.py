from models import storage
from api.v1.views import app_views
from flask import Flask
from flask_restful import Api, Resource
from os import environ

app = Flask(__name__)
api =Api(app)

app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage():
    """ it calls storage.close"""
    return storage.close()

@app.errorhandler(404)
def not_found_error(error):
    """return 404 status code response"""
    return make_response(jsonify({"error": "Not found"}), 404)





if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
