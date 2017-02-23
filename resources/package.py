from flask_restful import Resource, Api, reqparse, abort, request
from masheryapi.services.v3.base import Base
import logging

class Package(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, help='token', location='headers', required=True)

        args = parser.parse_args()

        mashery_v3 = Base('https', 'api.mashery.com', 'APIDefinitionImporter')        
        try:
            items = mashery_v3.fetch(args.token, '/packages', '')
            print items.json()
        except ValueError as err:
            abort(500, message=err.args)

        return items.json()

