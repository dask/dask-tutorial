## `dask` tutorial

*Matthew Rocklin*

Continuum Analytics

    git clone http://github.com/ContinuumIO/dask-tutorial
    cd dask-tutorial
    python prep.py  # create artificial datasets

    conda install dask pandas
    pip install castra graphviz  # optional


### **tl;dr**: `dask` enables parallel computing

### on larger-than-memory data


### High Level: `dask` collections mimic known libraries

*  `dask.array` = `numpy` + `threading`
*  `dask.dataframe` = `pandas` + `threading`
*  `dask.bag` = `map, filter, ...` + `multiprocessing`

<hr>

### Low Level: `dask` schedulers provide custom parallelism

*  Dynamic and low-latency
*  Memory aware
*  Accessible
*  Arbitrary and simple graph structure


*  High level NumPy/Pandas code

        x.dot(y) - y.mean(axis=0)
        df.groupby(df.name).amount.mean()

*  Creates task graph with dependencies

<img src="images/fail-case.png" width=50%>

*  Schedulers execute task graph

<img src="images/fail-case.gif" width=50%>


### Goals

*  High Level: Learn `dask.array/dataframe/bag`

    to handle 10-100GB datasets on a single machine

*  Low Level: Learn dynamic task scheduling

    to solve custom problems

<hr>

### Outline

1.  `dask.array` (high)
2.  Foundations (low)
3. `dask.dataframe` (high)
4.  Custom algorithms (low)
5.  `dask.bag` (high)
