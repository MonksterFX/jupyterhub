FROM jupyter/base-notebook:lab-2.0.1

RUN conda install --quiet --yes \
	numpy \
	pandas \
	matplotlib

RUN conda install --quiet --yes -c conda-forge \
	nodejs \
	faker \
	&& jupyter labextension install @jupyter-widgets/jupyterlab-manager \
	&& conda clean --all -f -y

COPY --chown=1000:100 work /home/jovyan/work

USER jovyan