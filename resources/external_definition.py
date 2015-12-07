from flask_restful import Resource, Api, reqparse, abort
from masheryapi.services.v3.base import Base
from masheryapi.services.v3.auth import Auth
from masheryapi.scripts.import_external_api_definitions import ImportExternalApiDefinitions
import logging

class ExternalDefinition(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('mashery_access_token', type=str, help='token',required=True)
        parser.add_argument('public_domain', type=str, help='Public domain to use for the new api', required=True)
        parser.add_argument('external_source', type=str, help='Location of the external api definition', required=True)
        parser.add_argument('create_package', type=str, help='Create a package for the new api', required=True)
        parser.add_argument('create_iodoc', type=str, help='Create an iodoc for the new api', required=True)

        args = parser.parse_args()
        mashery_v3 = Base('https', 'api.mashery.com', 'APIDefinitionImporter')        
        import_external_api_definitions = ImportExternalApiDefinitions(mashery_v3)

        try:
            imported_definition = import_external_api_definitions.import_definition(access_token, args.external_source, args.public_domain, args.create_package, args.create_iodoc)

        except ValueError as err:
            abort(500, message=err.args)
        
        return imported_definition

