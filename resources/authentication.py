import os
from flask_restful import Resource, Api, reqparse, abort
from masheryapi.services.v3.auth import Auth

class Authentication(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('area_id', type=str, help='ID of the Mashery Area', required=True)
        parser.add_argument('area_uuid', type=str, help='UUID of the Mashery Area', required=True)
        parser.add_argument('username', type=str, help='username', required=True)

        args = parser.parse_args()
        apikey = os.environ['MASHERY_API_KEY']#'mgmxvzspbh9d4wwncder4u62'
        secret = os.environ['MASHERY_API_SECRET']#'wtYsDAryQM'
        redirect_uri = os.environ['MASHERY_REDIRECT_URI']#'https://www.mashery.com'

        mashery_auth = Auth('https', 'api.mashery.com', args.area_id, args.area_uuid, apikey, secret, 'APIDefinitionImporter')
        try:
            auth_code = mashery_auth.get_authorization_code('qzwwye5qd9yyshzjzbjyuupn', apikey, redirect_uri, args.area_uuid, args.username)
            access_token = mashery_auth.get_access_token(auth_code, args.area_uuid, redirect_uri)
        except ValueError as err:
            abort(500, message=err.args)

        return access_token['token']
