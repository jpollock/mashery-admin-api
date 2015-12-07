from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from resources.external_definition import ExternalDefinition
from resources.authentication import Authentication

app = Flask(__name__)
api = Api(app)

api.add_resource(Authentication, '/authentication')
api.add_resource(ExternalDefinition, '/api_definitions')

if __name__ == '__main__':
    app.run(debug=True)
