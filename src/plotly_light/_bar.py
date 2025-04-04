from typing import Optional, Sequence

import plotly.graph_objects as go


def bar(
    x: Sequence,
    y: Sequence,
    text: Optional[Sequence] = None,
    horizontal_plot: bool = False,
    width: Optional[int] = None,
    col: Optional[str] = None,
    line_width: Optional[int] = None,
    line_col: Optional[str] = None,
    opacity: float = 1,
    name: Optional[str] = None,
    show_legend: bool = False,
    show_init: bool = True,
) -> go.Bar:
    """Create a simple Trace object of a histogram.

    positional arguments:
      @ x : Coordinates of data on x-axis.
      @ y : Coordinates of data on y-axis.

    optional arguments:
      @ col         : Color of bars.
      @ opacity     : Opacity of bars.
      @ name        : Display name of the trace in legend.
      @ show_legend : Show this trace in legend.
      @ show_init   : Show this trace initially.
    """
    return go.Bar(
        x=x,
        y=y,
        text=text,
        orientation="h" if horizontal_plot else None,
        width=width,
        marker=dict(
            color=col,
            line=dict(
                color=line_col,
                width=line_width,
            ),
        ),
        opacity=opacity,
        name=name,
        showlegend=show_legend,
        visible=None if show_init else "legendonly",
    )
