from typing import Union, Optional, Sequence, Tuple
import plotly.graph_objects as go


def make_scatter(x: Sequence,
                 y: Sequence,
                 text: Optional[Sequence] = None,
                 text_pos: Optional[str] = None,
                 text_size: Optional[float] = None,
                 text_col: Optional[str] = None,
                 mode: str = "markers",
                 marker_size: float = 5,
                 marker_width: int = None,
                 line_width: float = 1,
                 col: Optional[Union[str, Sequence[str]]] = None,
                 col_range: Optional[Tuple[float, float]] = None,
                 col_scale: Optional[str] = None,
                 reverse_scale: bool = False,
                 show_scale: bool = True,
                 name: Optional[str] = None,
                 show_legend: bool = False,
                 use_webgl: bool = True) -> go.Scatter:
    """Create a simple Trace object of a scatter plot.

    positional arguments:
      @ x : Coordinates of data on x-axis.
      @ y : Coordinates of data on y-axis.

    optional arguments:
      @ text          : Texts for each data.
      @ text_pos      : Specify positions of `text`.
                        Format is: "[top|middle|bottom] [left|center|right]".
      @ text_size     : Size of `text`.
      @ text_col      : Color of `text`.
      @ mode          : "markers", "lines", "markers+lines", "text", etc.
      @ marker_size   : For "markers" mode.
      @ marker_width  : For "markers" mode.
      @ line_width    : For "lines" mode.
      @ col           : Color of markers and lines.
      @ col_range     : Value range for color scale.
      @ col_scale     : Color scale for markers and lines.
      @ reverse_scale : Reverse `col_scale`.
      @ show_scale    : Show a scale bar for `col_scale`.
      @ name          : Display name of the trace in legend.
      @ show_legend   : Show this trace in legend.
      @ use_webgl     : Use WebGL instead of SVG for speed.
    """
    assert len(x) == len(y), "`x` and `y` must have same size"
    if text is not None:
        assert len(x) == len(text), "`text` must have same size as data"
    return (go.Scattergl if use_webgl else go.Scatter)(
        x=x,
        y=y,
        text=text,
        mode=mode,
        name=name,
        hoverinfo="text" if text is not None else None,
        textposition=text_pos,
        textfont=dict(size=text_size,
                      color=text_col),
        marker=(None if mode == "lines" else
                dict(size=marker_size,
                     color=col,
                     cmin=col_range[0] if col_range is not None else None,
                     cmax=col_range[1] if col_range is not None else None,
                     colorscale=col_scale,
                     reversescale=reverse_scale,
                     showscale=show_scale if col_scale is not None else None,
                     line=dict(width=marker_width))),
        line=(None if mode == "markers" else
              dict(width=line_width,
                   color=col)),
        showlegend=show_legend)
