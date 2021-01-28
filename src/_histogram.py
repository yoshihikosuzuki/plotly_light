from typing import Any, Union, Optional, Sequence, Mapping
from numbers import Number
from collections import Counter
import numpy as np
import plotly.graph_objects as go
from bits.util import RelCounter
from ._bar import make_bar
from ._scatter import make_scatter


def make_hist(data: Union[Sequence, Mapping[Any, int]],
              start: Optional[int] = None,
              end: Optional[int] = None,
              bin_size: Optional[int] = None,
              bin_num: int = 10,
              relative: bool = False,
              col: Optional[str] = None,
              opacity: float = 1,
              name: Optional[str] = None,
              show_legend: bool = False,
              show_init: bool = True,
              line_plot: bool = False,
              line_width: float = 1,
              use_webgl: bool = False,
              use_histogram: bool = False) -> Union[go.Bar, go.Histogram]:
    """Create a simple Trace object of a histogram.

    positional arguments:
      @ data : Raw data of numbers or counter of numbers

    optional arguments:
      @ start         : Start position of the plot range.
      @ end           : End position of the plot range.
      @ bin_size      : Size of each bin.
      @ bin_num       : Number of bins. Ignored if `bin_size` is set.
      @ relative      : Convert values in y-axis to relative frequencies.
      @ col           : Color of bars.
      @ opacity       : Opacity of bars.
      @ name          : Display name of the trace in legend.
      @ show_init       : Show this trace initially.
      @ show_legend   : Show this trace in legend.
      @ line_plot     : Draw as a line plot instead of a bar plot.
      @ line_width    : Valid only if `line_plot` is True.
      @ use_webgl     : Valid only if `line_plot` is True.
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
                            histnorm="percent" if relative else "",
                            marker=dict(color=col),
                            opacity=opacity,
                            name=name,
                            showlegend=show_legend,
                            visible=None if show_init else "legendonly")
    # Already a dictionary (counter), or non-numerical, categorical data
    if isinstance(data, Mapping) or not isinstance(next(iter(data)), Number):
        counter = RelCounter(data)
        if relative:
            counter = counter.relative()
        return (make_bar(**dict(zip(('x', 'y'),
                                    zip(*counter.items()))),
                         col=col,
                         opacity=opacity,
                         name=name,
                         show_legend=show_legend,
                         show_init=show_init)
                if not line_plot else
                make_scatter(**dict(zip(('x', 'y'),
                                        zip(*counter.items()))),
                             col=col,
                             opacity=opacity,
                             mode="lines",
                             line_width=line_width,
                             name=name,
                             show_legend=show_legend,
                             show_init=show_init,
                             use_webgl=use_webgl))
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
                                     weights=(np.ones(len(data))/float(len(data))
                                              if relative else None),
                                     range=(start - bin_size / 2,
                                            end + bin_size / 2),
                                     bins=bin_num)
    return (make_bar(x=[(bin_edges[i] + bin_edges[i + 1]) / 2
                        for i in range(len(bin_edges) - 1)],
                     y=counts,
                     col=col,
                     opacity=opacity,
                     name=name,
                     show_legend=show_legend,
                     show_init=show_init)
            if not line_plot else
            make_scatter(x=[(bin_edges[i] + bin_edges[i + 1]) / 2
                            for i in range(len(bin_edges) - 1)],
                         y=counts,
                         col=col,
                         opacity=opacity,
                         mode="lines",
                         line_width=line_width,
                         name=name,
                         show_legend=show_legend,
                         show_init=show_init,
                         use_webgl=use_webgl))
