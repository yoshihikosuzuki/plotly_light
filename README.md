# plotly_light

A wrapper of Plotly Python aiming for lightweight plots and ease of use.

## Why yet another wrapper?

The major reason is: _to reduce plot data size_.

Plotly officialy provides a utility wrapper named Plotly Express, and even without it, it is not so much difficult to write Plotly codes. However, the problem is the **embedded raw data** and the resulting **large data size** especially when you draw plots of large datasets. For example, when I draw a histogram, what I wish to see are essentially aggregated count values for each bin/label, but the histogram function of Plotly keeps all the raw data in the plot, which results in a heavy output file size and slow, painful interactive experience. I believe this behavior must come from Plotly's philosophy and do not wish to deny it, but I just want to have yet another wrapper simply for lightweight plots.

## Requirements

- Python >= 3 ([CPython](https://github.com/python/cpython) is recommended)

## How to install

```bash
$ git clone https://github.com/yoshihikosuzuki/plotly_light
$ cd plotly_light
$ python setup.py install
```

## How to use (in Jupyter Notebook)

```python
import plotly_light as pl

# Generate a histgram trace
trace = pl.make_hist([1, 2, 3, 2], bin_size=1)

# Draw the histogram with a default layout
pl.show(trace)

# Or you can make a custom layout
layout = pl.make_layout(x_title="x", y_title="y", x_range=(0, 10))

# And draw a plot with the custom layout
pl.show(trace, layout)
```

## List of functions

Every function named `XXX` can be called as `pl.XXX`, and in Jupyter Notebook, you can see the list of available functions via completion by pressing `TAB` after typing `pl.` as follows:

<img src="assets/jupyter_completion.png" width="300">

Below are short descriptions of each function by their type. For details, read the docstring of each function by e.g. running `pl.XXX?` in Jupyter Notebook. Below is an example with `pl.make_hist`:

<img src="assets/function_help.png" width="500">

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
  - Load and show a (zoomable) image file.
