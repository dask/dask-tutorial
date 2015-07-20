Dask Tutorial
=============

Dask provides multi-core execution on larger-than-memory datasets.

We can think of dask at a high and a low level

*  **High level:**  Dask provides high-level Array, DataFrame collections that
    mimic NumPy, and Pandas but can operate in parallel on datasets that don't
    fit into main memory.
*  **Low Level:** Dask provides dynamic task schedulers that can execute
   complex graphs of tasks with data dependencies.  These execution engines run
   the high-level collections but can also be used for other custom workloads.
   These schedulers are low-latency (around 1ms) and work hard to run
   computations in a small memory footprint.

Different users operate at different levels but it is useful to understand
both.  This tutorial will interleave between high-level use of `dask.array` and
`dask.dataframe` (even sections) and low-level use of dask graphs and
schedulers (odd sections.)

Links
-----

*  [Code](https://github.com/ContinuumIO/dask/)
*  [Docs](https://dask.pydata.org/en/latest/)

Outline
-------

0.  Dask Arrays

    *  [Arrays](00-Array.ipynb)

1.  Dask graphs and other fundamentals

    *  [Foundations](01-Foundations.ipynb)

2.  Tabular compuations with DataFrames

    *  [DataFrames](02-DataFrame.ipynb)
    *  [DataFrame Storage](03-DataFrame-Storage.ipynb)

3.  Imperative Programming

    *  [Imperative - `do`](04-Imperative.ipynb)

4.  Semi-structured data with Bag

    *  ...

5.  Graph analysis, optimization, and diagnostics

    *  ...
