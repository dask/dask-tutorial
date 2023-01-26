# Dask Tutorial

This tutorial was last given at SciPy 2022 in Austin Texas.
[A video of the SciPy 2022 tutorial is available online](https://youtu.be/J0NcbvkYPoE).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dask/dask-tutorial/main?urlpath=lab)
[![Build Status](https://github.com/dask/dask-tutorial/workflows/CI/badge.svg)](https://github.com/dask/dask-tutorial/actions?query=workflow%3ACI)

Dask is a parallel and distributed computing library that scales the existing Python and PyData ecosystem. Dask can scale up to your full laptop capacity and out to a cloud cluster.

## Prepare

#### 1. You should clone this repository

    git clone http://github.com/dask/dask-tutorial

and then install necessary packages.
There are three different ways to achieve this, pick the one that best suits you, and ***only pick one option***.
They are, in order of preference:

#### 2a) Create a conda environment (preferred)

In the main repo directory

    conda env create -f binder/environment.yml
    conda activate dask-tutorial

#### 2b) Install into an existing environment

You will need the following core libraries

    conda install -c conda-forge ipycytoscape jupyterlab python-graphviz matplotlib zarr xarray pooch pyarrow s3fs scipy dask distributed dask-labextension

Note that these options will alter your existing environment, potentially changing the versions of packages you already
have installed.

#### 2c) Use Dockerfile

You can build a docker image from the provided Dockerfile.

    $ docker build . # This will build using the same env as in a)

Run a container, replacing the ID with the output of the previous command

    $ docker run -it -p 8888:8888 -p 8787:8787 <container_id_or_tag>

The above command will give an URL (`Like http://(container_id or 127.0.0.1):8888/?token=<sometoken>`) which
can be used to access the notebook from browser. You may need to replace the given hostname with "localhost" or
"127.0.0.1".

#### You should follow only one of the options above!

### Launch Jupyter

From the repo directory

    jupyter lab

This was already done for method c) and does not need repeating.

You are welcome to use Jupyter notebook if you prefer, but we'll be using lab in the live tutorial.

## Links

*  Reference
    *  [Docs](https://dask.org/)
    *  [Examples](https://examples.dask.org/)
    *  [Code](https://github.com/dask/dask/)
    *  [Blog](https://blog.dask.org/)
*  Ask for help
    *   [`dask`](http://stackoverflow.com/questions/tagged/dask) tag on Stack Overflow, for usage questions
    *   [github issues](https://github.com/dask/dask/issues/new) for bug reports and feature requests
    *   [discourse forum](https://dask.discourse.group/) for general, non-bug, questions and discussion
    *   Attend a live tutorial

## Outline

0. [Overview](00_overview.ipynb) - dask's place in the universe.

1. [Dataframe](01_dataframe.ipynb) - parallelized operations on many pandas dataframes spread across your cluster.

2. [Array](02_array.ipynb) - blocked numpy-like functionality with a collection of numpy arrays spread across your cluster.

3. [Delayed](03_dask.delayed.ipynb) - the single-function way to parallelize general python code.

4. [Deployment/Distributed](04_distributed.ipynb) - Dask's scheduler for clusters, with details of how to view the UI.

5. [Distributed Futures](05_futures.ipynb) - non-blocking results that compute asynchronously.

6. Conclusion
