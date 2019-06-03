FROM jupyter/scipy-notebook

USER root
# python3 setup
RUN apt-get update && apt-get install -y graphviz

USER jovyan

RUN git clone https://github.com/dask/dask-tutorial.git ./dask-tutorial
RUN cd dask-tutorial && conda env update && python prep.py && cd ..
