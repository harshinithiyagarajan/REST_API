from flask import Flask,Blueprint,jsonify
from flask_cors import CORS

from api_sample.endpoints import rest_api

def create():
    web=Flask(__name__)
    CORS(web)

    api_blueprint=Blueprint('api_blueprint',__name__)
    api_blueprint=rest_api(api_blueprint)

    web.register_blueprint(api_blueprint,url_prefix='/api')

    return web


app=create()
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
