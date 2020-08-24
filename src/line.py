from typing import Optional, Tuple, List, Dict
import plotly.graph_objects as go
from .scatter import make_scatter


def make_line(x0: float, y0: float, x1: float, y1: float,
              width: float = 1,
              col: str = "black",
              layer: str = "above") -> Dict:
    """Create a (non-interactive) line-shape object.

    positional arguments:
      @ [x|y][0|1] : A line is drawn from (x0, y0) to (x1, y1).

    optional arguments:
      @ width : Line width.
      @ col   : Line color.
      @ layer : Drawing layer. Must be one of {'above', 'below'}.
    """
    assert layer in ("above", "below"), \
        "`layer` must be one of {'above' or 'below'}"
    return dict(type="line",
                xref="x",
                yref="y",
                x0=x0,
                y0=y0,
                x1=x1,
                y1=y1,
                line=dict(color=col,
                          width=width),
                layer=layer)


def make_lines(coords: List[Tuple[int, int, int, int]],
               width: float = 1,
               col: str = "black",
               name: Optional[str] = None,
               show_legend: bool = False) -> List[go.Scatter]:
    """A collection of lines with same width and color as a single trace.
    Use for lines with multiple types of width and/or color.

    positional arguments:
      @ coords : Coordinates `List[(x0, y0, x1, y1)]`.

    optional arguments:
      @ width       : Line width applied to all lines.
      @ col         : Line color applied to all lines.
      @ name        : Display name of the trace in legend.
      @ show_legend : Show this trace in legend.
    """
    return make_scatter(x=[x for x0, _, x1, _ in coords
                           for x in (x0, x1, None)],
                        y=[y for _, y0, _, y1 in coords
                           for y in (y0, y1, None)],
                        mode="lines",
                        line_width=width,
                        col=col,
                        name=name,
                        show_legend=show_legend)
