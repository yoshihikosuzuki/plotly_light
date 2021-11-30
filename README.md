# Plotly Light

A wrapper of Plotly Python aiming for lightweight plots and ease of use.

## Main features

:heavy_check_mark: **[SMALL FILE SIZE]** Plotly Light does not keep all raw data for a bar plot including a histogram, meaning you can keep the file size of a Jupyter Notebook file or a HTML file containing the plot very small even when drawing a histogram with a huge dataset.

:heavy_check_mark: **[COMPREHENSIBLE FUNCTION ARGUMENTS]** All positional and optional arguments of the functions in Plotly Light are explicitly written (without using `*args` nor `**kwargs`), meaning you can easily find an argument you want by peeking the definition and docstring of a function (which is a feature typically provided by Jupyter Notebook and other editors).

:x: **[LIMITED FEATURES AVAILABLE]** We provide only basic plotting functions and features, meaning not everything you can do with the original Plotly can be done with Plotly Light. However, Plotly Light is usually sufficient for most of the simple purposes.

## Requirements

- Python >= 3.7 ([CPython](https://github.com/python/cpython) is recommended)
- Other required Python packages are specified in `setup.cfg` and installed automatically.

## How to install

```bash
$ git clone https://github.com/yoshihikosuzuki/plotly_light
$ cd plotly_light
$ python setup.py install
```

## Usage example: Drawing a simple histogram in a Jupyter Notebook

All you need to use Plotly Light is to run the following single line (We strongly recommend this alias just like `numpy` and `pandas`). You do not have to run `init_notebook_mode(connected=True)` and so on because it is controled with a different function, `pl.set_default_renderer`, as described in the next section (Usually you do not need to care about it).

```python
import plotly_light as pl
```

The code below draws a histgram of many random numbers. You can confirm the file size does not increase even with a very large `k`, the number of data. With the original Plotly, the file size increases in proportion to the data size.

```python
import random
data = random.choices(list(range(10)), k=10000)
trace = pl.hist(data, bin_size=1)
pl.show(trace)
```

<img src="assets/example_hist1.png" width="800">

By default, the legend is not shown. You can show it with arbitrary name of the histogram:

```python
trace = pl.hist(data, bin_size=1, name="Random", show_legend=True)
pl.show(trace)
```

<img src="assets/example_hist2.png" width="800">

You can also use a custom layout

```python
layout = pl.layout(x_title="Number", y_title="Frequency", x_reversed=True)
pl.show(trace, layout)
```

<img src="assets/example_hist3.png" width="800">

## Changing the default theme, renderer, and layout

PLotly Light's default theme is `plotly_white` (with a custom color set), and its default renderer is `plotly_mimetype+notebook_connected` if the code is running in Jupyter or IPython and otherwise automatically determined. You can change them as follows:

```python
pl.set_default_theme("ggplot2")
pl.set_default_renderer("iframe_connected")
```

[TODO: how to get current default XXX? how to show the list of available XXX?]

[TODO: how to change color set?]

The list of availble themes and renderers can be shown by:

```python
```

You can also modify the default layout (e.g. fonts and margins) for plots. The default layout is specified in `src/__init__.py` as follows:

```python
set_default_layout(layout(font="Arial",
                          font_col="black",
                          font_size_title=20,
                          font_size_axis_title=18,
                          font_size_axis_tick=15,
                          font_size_legend=15,
                          margin=dict(l=10, r=10, t=30, b=10)))
```

and you can change it by running `pl.set_default_layout(pl.layout(<your favorite configurations>))`.

## List of functions

Every function/type named `XXX` offered by the package can be called as `pl.XXX`, and in Jupyter Notebook, you can see the list of available functions via completion by pressing `TAB` after typing `pl.` as follows:

<img src="assets/jupyter_completion.png" width="300">

Below are short descriptions of each function by their type. For details, read the docstring of each function by e.g. running `pl.XXX?` in Jupyter Notebook. Below is an example with `pl.make_hist`:

<img src="assets/function_help.png" width="500">

[TODO: example image of the plot by default for each plotting function]

### Traces

- `make_hist`
  - Lightweight histogram using a `go.Bar` instead of `go.Histogram`.
- `make_scatter`
  - Wrapper for `go.Scatter`.
- `make_lines`
  - For line(s) especially with multiple types of widths and/or colors.
  - Can also be generated as `shapes` in `go.Layout`, although traces are more lightweight when the number of lines is large.

### Shapes

- `make_rect`
  - Utility for generating a rectangle shape object.

### Layout

- `make_layout`
  - Utility for a `go.Layout` object.

### Figure

- `make_figure`
  - Wrapper of `go.Figure`.

### Drawing a plot

- `show`
  - Wrapper of `fig.show`.
- `show_image`
  - Load and show a (zoomable by default) image file.

### Configuration (see `How to use` section above)

- `set_default_theme`
- `set_default_layout`
- `set_default_renderer`
