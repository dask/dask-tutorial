# Dask Tutorial

This tutorial was last given at SciPy 2017 in Austin Texas.
[A video is available online](https://www.youtube.com/watch?v=mbfsog3e5DA).

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

#### a) Create a conda environment (preferred)

In the repo directory

    conda env create -f environment.yml 
    conda activate dask-tutorial

#### b) Install into an existing environment

You will need the following core libraries

    conda install numpy pandas h5py Pillow matplotlib scipy toolz pytables snakeviz dask distributed

You may find the following libraries helpful for some exercises

    pip install graphviz
    
#### c) Use Dockerfile

You can build a docker image out of the provided Dockerfile.



#### Graphviz on Windows

You may need to do install the dependencies like this:

    conda install -c conda-forge graphviz
    conda install -c conda-forge python-graphviz



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
    *   [`dask`](http://stackoverflow.com/questions/tagged/dask) tag on Stack Overflow, for usage questions
    *   [github issues](https://github.com/dask/dask/issues/new) for bug reports and feature requests
    *   [gitter chat](https://gitter.im/dask/dask) for general, non-bug, discussion
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
