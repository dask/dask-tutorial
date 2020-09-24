FROM jupyter/scipy-notebook:1386e2046833

USER root
# python3 setup
RUN apt-get update && apt-get install -y graphviz

USER jovyan

RUN git clone https://github.com/dask/dask-tutorial.git ./dask-tutorial
RUN cd dask-tutorial && conda env update -f binder/environment.yml && cd ..
RUN rm dask-tutorial/github_deploy_key_dask_dask_tutorial.enc

# The notebooks are configured to use kernel python3
# We want them to use the kernel dask-tutorial
# So we switch kernels

SHELL ["conda","run","-n","dask-tutorial","/bin/bash","-c"]
RUN . dask-tutorial/binder/postBuild
RUN jupyter kernelspec remove -f python3
RUN python -m ipykernel install --user --name python3 --display-name "Python 3"

# Shell into the container takes us to the correct environment

RUN conda init
RUN echo "conda activate dask-tutorial" >> ~/.bashrc

