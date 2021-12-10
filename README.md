# Dask Tutorial

This tutorial was last given at SciPy 2020 which was a virtual conference.
[A video of the SciPy 2020 tutorial is available online](https://www.youtube.com/watch?v=EybGGLbLipI).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dask/dask-tutorial/main?urlpath=lab)
[![Build Status](https://github.com/dask/dask-tutorial/workflows/CI/badge.svg)](https://github.com/dask/dask-tutorial/actions?query=workflow%3ACI)

Dask provides multi-core execution on larger-than-memory datasets.

We can think of dask at a high and a low level

*  **High level collections:**  Dask provides high-level Array, Bag, and DataFrame
   collections that mimic NumPy, lists, and Pandas but can operate in parallel on
   datasets that don't fit into main memory.  Dask's high-level collections are
   alternatives to NumPy and Pandas for large datasets.
*  **Low Level schedulers:** Dask provides dynamic task schedulers that
   execute task graphs in parallel.  These execution engines power the
   high-level collections mentioned above but can also power custom,
   user-defined workloads.  These schedulers are low-latency (around 1ms) and
   work hard to run computations in a small memory footprint.  Dask's
   schedulers are an alternative to direct use of `threading` or
   `multiprocessing` libraries in complex cases or other task scheduling
   systems like `Luigi` or `IPython parallel`.

Different users operate at different levels but it is useful to understand
both.  This tutorial will interleave between high-level use of `dask.array` and
`dask.dataframe` (even sections) and low-level use of dask graphs and
schedulers (odd sections.)

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
    jupyter labextension install dask-labextension
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install @bokeh/jupyter_bokeh

#### 2b) Install into an existing environment

You will need the following core libraries

    conda install numpy pandas h5py pillow matplotlib scipy toolz pytables snakeviz scikit-image dask distributed -c conda-forge

You may find the following libraries helpful for some exercises

    conda install python-graphviz -c conda-forge

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

### Launch notebook

From the repo directory

    jupyter notebook

Or

    jupyter lab

This was already done for method c) and does not need repeating.

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

1. [Delayed](01_dask.delayed.ipynb) - the single-function way to parallelize general python code.

1x. [Lazy](01x_lazy.ipynb) - some of the principles behind lazy execution, for the interested.

2. [Bag](02_bag.ipynb) - the first high-level collection: a generalized iterator for use
with a functional programming style and to clean messy data.

3. [Array](03_array.ipynb) - blocked numpy-like functionality with a collection of
numpy arrays spread across your cluster.

7. [Dataframe](04_dataframe.ipynb) - parallelized operations on many pandas dataframes
spread across your cluster.

5. [Distributed](05_distributed.ipynb) - Dask's scheduler for clusters, with details of
how to view the UI.

6. [Advanced Distributed](06_distributed_advanced.ipynb) - further details on distributed
computing, including how to debug.

7. [Dataframe Storage](07_dataframe_storage.ipynb) - efficient ways to read and write
dataframes to disc.

8. [Machine Learning](08_machine_learning.ipynb) - applying dask to machine-learning problems.
