# plotly_light

A python Plotly wrapper aiming for lightweight plots

## Why yet another wrapper?

In short: _to reduce plot data size_.

Plotly officialy provides a utility wrapper named Plotly Express, and even without it, it is not so much difficult to write Plotly codes. However, the problem is the **embedded raw data** and the resulting **large data size** especially when you draw plots of large datasets. For example, when I draw a histogram, what I wish to see are essentially aggregated count values for each label, but the histogram function of Plotly keeps all the raw data in the plot, which results in a heavy output file size and slow, painful interactive experience. I believe this behavior must come from Plotly's philosophy, but I just want to have yet another wrapper simply for lightweight plots.

## Why not using other visualization tools?

I have a simple answer: I like the plots Plotly draws.

## Requirements

- Python >= 3

## How to install

```bash
$ git clone https://github.com/yoshihikosuzuki/plotly_light
$ cd plotly_light
$ python setup.py install
```

## How to use

```python
import plotly_light as pl

# Generate a histgram trace
trace = pl.make_histogram([1, 2, 3, 2], bin_size=1)

# Make a custom layout
layout = pl.make_layout(x_title="x", y_title="y", x_range=(0, 10))
```

If you are running inside Jupyter, you can plot as follows:

```python
# Draw the histogram with a default layout
pl.show_plot(trace)

# Or you can make a custom layout
pl.show_plot(trace, layout)
```

## List of functions

Every instance `XXX` below can be called as `pl.XXX`. For details, read the docstring of each function.

### Traces

- `make_hist`
  - Lightweight histogram using a barplot instead of histogram.
- `make_scatter`
  - Easy-to-use, but the return object is currently as large as that of Plotly.
- `make_lines`
  - For the "lines" mode of the scatter plot with multiple types of widths and/or colors.
  - More efficient in terms of data size than using shapes.

### Shapes

- `make_line`
  - Utility for generating a line shape object.
- `make_rect`
  - Utility for generating a rectangle shape object.

### Layout

- `make_layout`
  - Utility for generating a layout object.

### Drawing a plot

- `show_plot`
  - Utility for drawing a plot.
