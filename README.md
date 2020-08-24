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

```
