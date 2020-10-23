from typing import Union, Optional, Tuple, List, Dict
import plotly.graph_objects as go
from ._scatter import make_scatter

Coord = Tuple[int, int, int, int]


def make_lines(coords: Union[Coord, List[Coord]],
               width: float = 1,
               col: str = "black",
               by: str = "shape",
               xref: str = "x",
               yref: str = "y",
               layer: str = "above",
               name: Optional[str] = None,
               show_legend: bool = False,
               use_webgl: bool = True) -> List[go.Scatter]:
    """A collection of lines with same width and color.

    positional arguments:
      @ coords : (A list of) coordinate (x0, y0, x1, y1).

    optional arguments:
      @ width       : Line width applied to all lines.
      @ col         : Line color applied to all lines.
      @ by          : Must be one of {"shape", "trace"}.
      @ [x|y]ref    : Valid only if `by="shape"`.
                      Must be one of {'[x|y]', 'paper'}.
                      If "paper", values of `[x|y]0,1` must be within [0, 1]
                      and are interpreted as relative positions in the entire
                      [x|y]-axis.
      @ layer       : Valid only if `by="shape"`.
                      Drawing layer. Must be one of {'above', 'below'}.
      @ name        : Valid only if `by="trace"`.
                      Display name of the trace in legend.
      @ show_legend : Valid only if `by="trace"`.
                      Show this trace in legend.
      @ use_webgl   : Valid only if `by="trace"`.
                      Use WebGL instead of SVG.
    """
    def coord_to_shape(coord: Coord) -> Dict:
        x0, y0, x1, y1 = coord
        return dict(type="line",
                    xref=xref,
                    yref=yref,
                    x0=x0,
                    y0=y0,
                    x1=x1,
                    y1=y1,
                    line=dict(color=col,
                              width=width),
                    layer=layer)

    assert by in ("shape", "trace"), \
        "`by` must be 'shape' or 'trace'"
    assert xref in ("x", "paper") and yref in ("y", "paper"), \
        "`[x|y]ref` must be '[x|y]' or 'paper'"
    assert layer in ("above", "below"), \
        "`layer` must be one of {'above' or 'below'}"
    if by == "shape":
        return (coord_to_shape(coords) if not isinstance(coords, list)
                else list(map(coord_to_shape, coords)))
    else:
        if not isinstance(coords, list):
            coords = [coords]
        return make_scatter(x=[x for x0, _, x1, _ in coords
                               for x in (x0, x1, None)],
                            y=[y for _, y0, _, y1 in coords
                               for y in (y0, y1, None)],
                            mode="lines",
                            line_width=width,
                            col=col,
                            name=name,
                            show_legend=show_legend,
                            use_webgl=use_webgl)
