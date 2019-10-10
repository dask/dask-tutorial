FROM jupyter/scipy-notebook:1386e2046833

USER root
# python3 setup
RUN apt-get update && apt-get install -y graphviz

USER jovyan

RUN git clone https://github.com/dask/dask-tutorial.git ./dask-tutorial
RUN cd dask-tutorial && conda env update -f binder/environment.yml && . binder/postBuild && cd ..
RUN rm dask-tutorial/github_deploy_key_dask_dask_tutorial.enc
