[![PyPI version](https://badge.fury.io/py/plotly-light.svg)](https://badge.fury.io/py/plotly-light)
[![License](http://img.shields.io/badge/license-MIT-blue)](LICENSE)

# plotly_light

A wrapper of Plotly Python aiming for lightweight plots and ease of use.

## Main features

:heavy_check_mark: **[SMALLER PLOT SIZE]** Plotly Light does not keep all raw data for a bar plot including a histogram, meaning you can keep the file size of a Jupyter Notebook file or a HTML file containing the plot very small even when drawing a histogram with a huge dataset.

:heavy_check_mark: **[SEPARATE DIRECTORY FOR HTML PLOTS]** By default, each plot drawn by Plotly Light in a Jupyter Notebook is saved as a HTML file in a directory named `<notebook-basename>.iframe_figures/`, enabling us to keep the file size of a Notebook small and to easily obtain a single HTML file only of a plot. This feature can be disabled.

:heavy_check_mark: **[COMPREHENSIBLE FUNCTION ARGUMENTS]** All positional and optional arguments of the functions in Plotly Light are explicitly written (without using `*args` nor `**kwargs`), meaning you can easily find an argument you want by peeking the definition and docstring of a function (which is a feature typically provided by Jupyter Notebook and other editors).

:x: **[LIMITED FEATURES AVAILABLE]** We provide only basic plotting functions and features, meaning not everything you can do with the original Plotly can be done with Plotly Light. However, Plotly Light is usually sufficient for most of the simple purposes.

## Requirements

- Python >= 3.7 ([CPython](https://github.com/python/cpython) is recommended)

## How to install

### 1. Via PyPI (recommended)

```bash
$ pip install plotly-light
```

### 2. Via this GitHub repository

```bash
$ git clone https://github.com/yoshihikosuzuki/plotly_light
$ cd plotly_light
$ pip install .
```

## How to use

See [Reference](https://nbviewer.org/github/yoshihikosuzuki/plotly_light/blob/master/doc/Reference.ipynb).

