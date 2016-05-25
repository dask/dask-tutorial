Dask Tutorial
=============

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

Prepare
-------

You will need the following core libraries

    conda install numpy pandas h5py pil matplotlib scipy toolz matplotlib pytables

And a recently updated version of dask

    conda/pip install dask

You may find the following libraries helpful for some exercises

    pip install castra graphviz

You should clone this repository

    git clone http://github.com/dask/dask-tutorial

and then run this script to prepare artificial data.

    cd dask-tutorial
    python prep.py

Links
-----

*  Reference
    *  [Docs](https://dask.pydata.org/en/latest/)
    *  [Code](https://github.com/dask/dask/)
    *  [Blog](http://matthewrocklin.com/blog/)
*  Ask for help
    *   [`dask`](http://stackoverflow.com/questions/tagged/dask) tag on Stack Overflow
    *   [github issues](https://github.com/dask/dask/issues/new) for bug reports and feature requests
    *   [blaze-dev](http://groups.google.com/a/continuum.io/forum/#!forum/blaze-dev)  mailing list for community discussion
    *   Please ask questions during a live tutorial

Outline
-------

Introduction - [slides](http://dask.github.io/dask-tutorial/introduction.html)

1.  Arrays - [slides](http://dask.github.io/dask-tutorial/array.html)

    *  [Arrays](01-Array.ipynb)

2.  Task graphs and other fundamentals - [slides](http://dask.github.io/dask-tutorial/graphs.html)

    *  [Foundations](02-Foundations.ipynb)

3.  DataFrames

    *  [DataFrames](03a-DataFrame.ipynb)
    *  [DataFrame Storage](03b-DataFrame-Storage.ipynb)

4.  Imperative Programming

    *  [Imperative - `do`](04-Imperative.ipynb)

5.  Bags of semi-structured data

    *  [Bag - Parallel lists](05-Bag.ipynb)

6.  Homework - large datasets with which to play at home

    *  [Homework](Homework.ipynb)

End - [slides](http://dask.github.io/dask-tutorial/end.html)
