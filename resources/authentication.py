import os
from flask_restful import Resource, Api, reqparse, abort, request
from masheryapi.services.v3.auth import Auth

class Authentication(Resource):

    def post(self):
    
        parser = reqparse.RequestParser()
        #parser.add_argument('username', type=str, help='username', required=True)
        #parser.add_argument('password', type=str, help='password', required=True)
        #parser.add_argument('area_uuid', type=str, help='UUID of the Mashery Area', required=True)
        parser.add_argument('code', type=str, help='username', required=True)
        parser.add_argument('scope', type=str, help='password', required=True)

        args = parser.parse_args()
        apikey = os.environ['MASHERY_API_KEY']
        secret = os.environ['MASHERY_API_SECRET']
        redirect_uri = os.environ['MASHERY_REDIRECT_URI']

        mashery_auth = Auth('https', 'api.example.com', None, args.scope, apikey, secret, 'APIDefinitionImporter')
        #try:
            #access_token = mashery_auth.get_access_token(args.username, args.password, args.area_uuid)
        access_token = mashery_auth.get_access_token_with_code(args.code, args.scope, redirect_uri)
        #except ValueError as err:
        #    abort(500, message=err.args)

        return access_token
