FROM jupyter/base-notebook:lab-2.0.1

RUN conda install --quiet --yes \
	numpy \
	pandas \
	matplotlib \
	&& conda clean --all -f -y

USER jovyan
