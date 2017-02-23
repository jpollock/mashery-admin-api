from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from resources.external_definition import ExternalDefinition
from resources.format_to_api_definition import FormatToApiDefinition
from resources.format_to_iodoc_definition import FormatToIodocDefinition
from resources.authentication import Authentication
from resources.service import Service
from resources.package import Package
import logging

app = Flask(__name__)
api = Api(app)

api.add_resource(Authentication, '/authentication')
api.add_resource(ExternalDefinition, '/api_definitions')
api.add_resource(FormatToApiDefinition, '/format_to_api_definition')
api.add_resource(FormatToIodocDefinition, '/format_to_iodoc_definition')
api.add_resource(Service, '/services')
api.add_resource(Package, '/packages')

import logging

# Log only in production mode.
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
app.logger.addHandler(stream_handler)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
