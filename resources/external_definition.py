from flask_restful import Resource, Api, reqparse, abort
from masheryapi.services.v3.base import Base
from masheryapi.services.v3.auth import Auth
from masheryapi.scripts.import_external_api_definitions import ImportExternalApiDefinitions
import logging

class ExternalDefinition(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('area_id', type=str, help='ID of the Mashery Area')
        parser.add_argument('area_uuid', type=str, help='UUID of the Mashery Area')
        parser.add_argument('username', type=str, help='username')
        parser.add_argument('public_domain', type=str, help='Public domain to use for the new api')
        parser.add_argument('external_source', type=str, help='Location of the external api definition')
        parser.add_argument('create_package', type=str, help='Create a package for the new api')
        parser.add_argument('create_iodoc', type=str, help='Create an iodoc for the new api')

        args = parser.parse_args()
        if args.area_uuid == None or args.external_source == None or args.public_domain == None:
            abort(400, message="Missing parameter")

        apikey = 'mgmxvzspbh9d4wwncder4u62'
        secret = 'wtYsDAryQM'
        redirect_uri = 'https://www.mashery.com'

        mashery_v3 = Base('https', 'api.mashery.com', 'APIDefinitionImporter')
        mashery_auth = Auth('https', 'api.mashery.com', args.area_id, args.area_uuid, apikey, secret, 'APIDefinitionImporter')
        auth_code = mashery_auth.get_authorization_code('qzwwye5qd9yyshzjzbjyuupn', apikey, redirect_uri, args.area_uuid, args.username)
        access_token = mashery_auth.get_access_token(auth_code, args.area_uuid, redirect_uri)

        import_external_api_definitions = ImportExternalApiDefinitions(mashery_v3)

        try:
            imported_definition = import_external_api_definitions.import_definition(access_token, args.external_source, args.public_domain, args.create_package, args.create_iodoc)

        except ValueError as err:
            abort(500, message=err.args)
        
        return imported_definition

