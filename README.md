# Dask Tutorial

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

You should clone this repository

    git clone http://github.com/dask/dask-tutorial

and then install necessary packages.

### a) Install into an existing environment

You will need the following core libraries

    conda install numpy pandas h5py Pillow matplotlib scipy toolz pytables snakeviz dask distributed

You may find the following libraries helpful for some exercises

    pip install graphviz cachey
    
### b) Create a new environment

In the repo directory

    conda env create -f environment.yml 

and then on osx/linux

    source activate dask-tutorial

on windows

    activate dask-tutorial

### c) Use Dockerfile

You can build a docker image out of the provided Dockerfile.



### Graphviz on Windows

Windows users can install graphviz as follows

1. Install Graphviz from http://www.graphviz.org/Download_windows.php
2. Add C:\Program Files (x86)\Graphviz2.38\bin to the PATH

Alternatively one can use the following conda commands (one installs graphviz and one installs python-bindings for graphviz):

1. conda install -c conda-forge graphviz
2. conda install -c conda-forge python-graphviz



### Prepare artificial data.

From the repo directory

    python prep.py


### Launch notebook

From the repo directory

    jupyter notebook 


## Links

*  Reference
    *  [Docs](http://dask.pydata.org/en/latest/)
    *  [Code](https://github.com/dask/dask/)
    *  [Blog](http://matthewrocklin.com/blog/)
*  Ask for help
    *   [`dask`](http://stackoverflow.com/questions/tagged/dask) tag on Stack Overflow
    *   [github issues](https://github.com/dask/dask/issues/new) for bug reports and feature requests
    *   [blaze-dev](http://groups.google.com/a/continuum.io/forum/#!forum/blaze-dev)  mailing list for community discussion
    *   Please ask questions during a live tutorial

## Outline

1. [Overview](01_overview.ipynb) - dask's place in the universe

2. [Foundations](02_foundations.ipynb) - low-level Dask and how it does what it does

3. [Bag](03_bag.ipynb) - the first high-level collection: a generalized iterator for use
with a functional programming style and o clean messy data.
 
4. [Distributed](04_distributed.ipynb) - Dask's scheduler for clusters, with details of
how to view the UI.

5. [Array](05_array.ipynb) - blocked numpy-like functionality with a collection of 
numpy arrays spread across your cluster.

6. [Advanced Distributed](06_distributed_advanced.ipynb) - further details on distributed 
computing, including how to debug.

7. [Dataframe](07_dataframe.ipynb) - parallelized operations on many pandas dataframes
spread across your cluster.

8. [Dataframe Storage](08_dataframe_storage.ipynb) - efficient ways to read and write
dataframes to disc.
