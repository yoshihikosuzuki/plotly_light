from typing import Any, Union, Optional, Sequence, Mapping
from numbers import Number
from collections import Counter
import numpy as np
import plotly.graph_objects as go


def make_hist(data: Union[Sequence, Mapping[Any, int]],
              start: Optional[int] = None,
              end: Optional[int] = None,
              bin_size: Optional[int] = None,
              bin_num: int = 10,
              col: Optional[str] = None,
              name: Optional[str] = None,
              show_legend: bool = False,
              use_histogram: bool = False) -> Union[go.Bar, go.Histogram]:
    """Create a simple Trace object of a histogram.

    positional arguments:
      @ data : Raw data of numbers or counter of numbers

    optional arguments:
      @ start         : Start position of the plot range.
      @ end           : End position of the plot range.
      @ bin_size      : Size of each bin.
      @ bin_num       : Number of bins. Ignored if `bin_size` is set.
      @ name          : Display name of the trace in legend.
      @ show_legend   : Show this trace in legend.
      @ use_histogram : Force to use `go.Histogram`, not `go.Bar`.
    """
    # Use the original histogram function anyway (not recommended)
    if use_histogram:
        assert isinstance(data, Sequence), \
            "Only Sequence objects are supported if `use_histogram`."
        return go.Histogram(x=data,
                            xbins=dict(start=start,
                                       end=end,
                                       size=bin_size),
                            marker=dict(color=col),
                            name=name,
                            showlegend=show_legend)
    # Non-numerical, categorical data
    if isinstance(data, Mapping) or not isinstance(next(iter(data)), Number):
        counter = Counter(data) if isinstance(data, Sequence) else data
        return go.Bar(**dict(zip(('x', 'y'),
                                 zip(*counter.items()))),
                      width=bin_size,
                      marker_color=col,
                      name=name,
                      showlegend=show_legend)
    # Numerical data
    if start is None:
        start = min(data)
    if end is None:
        end = max(data)
    if bin_size is not None:
        bin_num = -int(-(end - start + bin_size) // bin_size)
    else:
        bin_size = (end - start) / bin_num
    counts, bin_edges = np.histogram(data,
                                     range=(start - bin_size / 2,
                                            end + bin_size / 2),
                                     bins=bin_num)
    return go.Bar(x=[(bin_edges[i] + bin_edges[i + 1]) / 2
                     for i in range(len(bin_edges) - 1)],
                  y=counts,
                  width=bin_size,
                  marker_color=col,
                  name=name,
                  showlegend=show_legend)
