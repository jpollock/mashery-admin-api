from flask_restful import Resource, Api, reqparse, abort, request
from masheryapi.services.v3.base import Base
import logging

class Service(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, help='token', location='headers', required=True)

        args = parser.parse_args()

        mashery_v3 = Base('https', 'api.mashery.com', 'APIDefinitionImporter')        
        try:
            services = mashery_v3.fetch(args.token, '/services', '')
            print services.json()
        except ValueError as err:
            abort(500, message=err.args)

        return services.json()

