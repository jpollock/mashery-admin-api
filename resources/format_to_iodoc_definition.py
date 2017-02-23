from flask import request
from flask_restful import Resource, Api, reqparse, abort
from masheryapi.services.v3.base import Base
from masheryapi.services.v3.auth import Auth
from masheryapi.services.v3.apis import Apis
import logging

class FormatToIodocDefinition(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('mashery_access_token', type=str, help='token',required=True)
        parser.add_argument('public_domain', type=str, help='Public domain to use for the new api', required=True)
        
        args = parser.parse_args()

        api_service = Apis()
        
        external_api_definition_content = request.get_json()

        if  external_api_definition_content == None:
            raise ValueError("External source cannot be retrieved or is invalid JSON.") 

        iodoc_definition = api_service.iodoc_from_swagger(args.public_domain, external_api_definition_content)

        if iodoc_definition == None:
            code = 500
            message = 'problem'

            abort(code, message=message)

        return iodoc_definition

