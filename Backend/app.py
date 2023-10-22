from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.ServiceRoutes import service_bp
app = Flask(__name__)
CORS(app)
api = Api(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,x-access-token,x-reset-token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

app.register_blueprint(service_bp, url_prefix='/service')


if __name__ == "__main__":
    app.run(debug=True)