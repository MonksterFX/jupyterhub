import json, os, urllib

# from tornado.auth import OAuth2Mixin
# from tornado import gen, web
# from tornado.httputil import url_concat
# from tornado.httpclient import HTTPRequest, AsyncHTTPClient

# from jupyterhub.auth import LocalAuthenticator
# from jupyterhub.handlers import LogoutHandler
# from jupyterhub.utils import url_path_join

# from oauthenticator.oauth2 import OAuthLoginHandler, OAuthenticator

# oidc_client_id = 'jupyterhub'

# class KeycloakMixin(OAuth2Mixin):

#      # oidc_server_host = os.getenv('DLA_KEYCLOAK_SCHEME_HOST')
#     oidc_server_host = "http://localhost:9080"
#     _OAUTH_AUTHORIZE_URL = "{}/auth/realms/{}/protocol/openid-connect/auth".format(oidc_server_host, oidc_client_id)
#     _OAUTH_ACCESS_TOKEN_URL = "{}/auth/realms/{}/protocol/openid-connect/token".format(oidc_server_host, oidc_client_id)
#     _OAUTH_LOGOUT_URL = "{}/auth/realms/{}/protocol/openid-connect/logout".format(oidc_server_host, oidc_client_id)
#     _OAUTH_USERINFO_URL = "{}/auth/realms/{}/protocol/openid-connect/userinfo".format(oidc_server_host, oidc_client_id)

# class KeycloakLoginHandler(OAuthLoginHandler, KeycloakMixin):
#     pass

# class KeycloakLogoutHandler(LogoutHandler, KeycloakMixin):
#     def get(self):
#         params = dict(
#             redirect_uri="%s://%s%slogout" % (
#                 self.request.protocol, self.request.host,
#                 self.hub.server.base_url)
#         )
#         logout_url = KeycloakMixin._OAUTH_LOGOUT_URL
#         logout_url = url_concat(logout_url, params)
#         self.redirect(logout_url, permanent=False)

# class KeycloakOAuthenticator(OAuthenticator, KeycloakMixin):
#     login_service = "OpenID Connect"
#     login_handler = KeycloakLoginHandler

#     def check_whitelist(self, username, authentication=None):
#         self.log.info('Checking whilelist for username: %r', username)
#         return True

#     def logout_url(self, base_url):
#         return url_path_join(base_url, 'oauth_logout')

#     def get_handlers(self, app):
#         handlers = OAuthenticator.get_handlers(self, app)
#         handlers.extend([(r'/oauth_logout', KeycloakLogoutHandler)])
#         return handlers

#     @gen.coroutine
#     def authenticate(self, handler, data=None):
#         code = handler.get_argument("code", False)
#         self.log.info('code: %s', code)
#         if not code:
#             raise web.HTTPError(400, "oauth callback made without a token")
#         http_client = AsyncHTTPClient()
#         params = dict(
#             grant_type='authorization_code',
#             code=code,
#             redirect_uri=self.get_callback_url(handler),
#         )
#         token_url = KeycloakMixin._OAUTH_ACCESS_TOKEN_URL
#         token_req = HTTPRequest(
#             token_url,
#             method="POST",
#             headers={
#                 "Accept": "application/json",
#                  "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
#             },
#             auth_username = self.client_id,
#             auth_password = self.client_secret,
#             body = urllib.parse.urlencode(params).encode('utf-8'),
#             )
            
#         self.log.info("".center(50, '-'))
#         self.log.info(token_url)
#         self.log.info(urllib.parse.urlencode(params).encode('utf-8'))
#         self.log.info("".center(50, '-'))
        
#         token_resp = yield http_client.fetch(token_req)
#         token_resp_json = json.loads(token_resp.body.decode('utf8', 'replace'))
#         access_token = token_resp_json['access_token']
#         if not access_token:
#             raise web.HTTPError(400, "failed to get access token")
#         self.log.info('oauth token: %r', access_token)
#         user_info_url = KeycloakMixin._OAUTH_USERINFO_URL
#         user_info_req = HTTPRequest(
#             user_info_url,
#             method="GET",
#             headers={
#                 "Accept": "application/json",
#                 "Authorization": "Bearer %s" % access_token
#                 },
#             )
#         user_info_res = yield http_client.fetch(user_info_req)
#         self.log.info('user_info_res: %r', user_info_res)
#         user_info_res_json = json.loads(user_info_res.body.decode('utf8', 'replace'))
#         self.log.info('user_info_res_json: %r', user_info_res_json)
#         return {
#             'name': user_info_res_json['preferred_username'],
#             'auth_state': {
#                 'upstream_token': user_info_res_json,
#             },
#         }

# class LocalKeycloakOAuthenticator(LocalAuthenticator, KeycloakOAuthenticator):
#     """A version that mixes in local system user creation"""
#     pass

#------------------------------ config ------------------------------

# load initial config
c = get_config()

# authentification
c.Authenticator.admin_users = { 'admin' }
# c.Authenticator.whitelist = whitelist = set()

# keycloak authentification
# c.JupyterHub.authenticator_class = KeycloakOAuthenticator

# from oauthenticator.generic import GenericOAuthenticator
# c.JupyterHub.authenticator_class = GenericOAuthenticator
# c.GenericOAuthenticator.oauth_callback_url = 'http://localhost:8000/hub/oauth_callback'
# c.GenericOAuthenticator.client_id = 'jupyterhub'
# c.GenericOAuthenticator.client_secret = 'f68220b6-6728-4722-86f7-9c2bdd222977'
# c.GenericOAuthenticator.token_url = 'http://localhost:9080/auth/realms/jupyterhub/protocol/openid-connect/token'
# c.GenericOAuthenticator.userdata_url = 'http://localhost:9080/auth/realms/jupyterhub/protocol/openid-connect/userinfo'
# c.GenericOAuthenticator.userdata_method = 'GET'
# c.GenericOAuthenticator.userdata_params: {'state': 'state'}
# c.GenericOAuthenticator.username_key: 'preferred_username'

# c.Authenticator.auto_login = True
# c.LocalAuthenticator.create_system_users = True

# hub config
## let admin access notebooks from students
c.JupyterHub.admin_access = True
c.JupyterHub.hub_ip = os.environ['HUB_IP']
# c.JupyterHub.hub_port = 8080

## spawning config

## use docker spawner for docker only
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']

c.Spawner.default_url = '/lab'

# Setting Enviroments for startup of lab
# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#docker-options
c.DockerSpawner.environment = {'CHOWN_HOME':'yes', 'CHOWN_HOME_OPTS':'-R', 'GRANT_SUDO':'yes'}

# persitency
## create volume to store at
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

## remove containers once they are stopped
c.DockerSpawner.remove_containers = True
