# jupyterhub on single maschine with docker
Single Docker Instanz + Jupyterhub + Jupyter Lab + Doc

Motivation behind this is a simple minimal running setup for small classes teaching python in jupyterhub. This includes:

* Traefik v2.1
* Jupyterhub 1.0.0 (docker image 1.1.0 actually not working)
* Basic modified JuypterLab image

## good reads before you start
* [Getting an overview](https://jupyterhub.readthedocs.io/en/stable/)

## jupterhub
ToDo: Jupyterhub image and how to modify, local PAM users only (if you do not have an oauth service), how to modify frontpage (Logo etc.), sso

## notebooks
ToDo: Own Image Creation, List of provided images

## usefull advices

### authentication
* [Authentication with Kubernetes Deployments](https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/authentication.html)
* [Keycloak Authenticator](https://github.com/jupyterhub/oauthenticator/pull/183)
