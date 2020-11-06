FROM jupyter/base-notebook:lab-2.2.5

USER root
# python3 setup
RUN apt-get update && apt-get install -y graphviz git

USER jovyan

RUN git clone https://github.com/dask/dask-tutorial.git ./dask-tutorial
RUN cd dask-tutorial && conda env update -n base -f binder/environment.yml --prune && . binder/postBuild && cd ..
RUN rm dask-tutorial/github_deploy_key_dask_dask_tutorial.enc
