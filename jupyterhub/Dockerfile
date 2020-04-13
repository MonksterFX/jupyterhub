FROM jupyterhub/jupyterhub:1.0.0

# add default admin with password admin
RUN useradd admin
RUN echo "admin:admin" | chpasswd

RUN pip install \
    dockerspawner==0.10.0 \ 
    oauthenticator==0.10

RUN apt-get update && apt-get install nano

COPY jupyterhub_config.py .
COPY scripts /scripts

