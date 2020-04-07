import os

# load initial config
c = get_config()

# authentification
c.Authenticator.admin_users = { 'admin' }
c.Authenticator.whitelist = whitelist = set()

# keycloak authentification
# from oauthenticator.generic import GenericOAuthenticator
# c.JupyterHub.authenticator_class = GenericOAuthenticator
# c.GenericOAuthenticator.oauth_callback_url = 'http://localhost:8000/hub/oauth_callback'
# c.GenericOAuthenticator.client_id = 'jupyterhub'
# c.GenericOAuthenticator.client_secret = os.environ['KC_SECRET']
# c.GenericOAuthenticator.token_url = 'http://localhost:9080/auth/realms/jupyterhub/protocol/openid-connect/token'
# c.GenericOAuthenticator.userdata_url = 'http://localhost:9080/auth/realms/jupyterhub/protocol/openid-connect/userinfo',
# c.GenericOAuthenticator.userdata_method = 'GET'
# c.GenericOAuthenticator.userdata_params: {'state': 'state'}
# c.GenericOAuthenticator.username_key: 'preferred_username'

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

# persitency
## create volume to store at
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/'
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

## remove containers once they are stopped
c.DockerSpawner.remove_containers = True
