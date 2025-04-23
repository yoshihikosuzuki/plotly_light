from typing import Dict, List, Optional, Sequence, Tuple, Union

import plotly.graph_objects as go

from ._scatter import scatter

Coord = Tuple[int, int, int, int]
Point = Tuple[int, int]


def closures(
    coords: Union[List[Point], List[List[Point]]],
    frame_width: float = 1,
    frame_col: Optional[str] = "black",
    fill_col: Optional[str] = "gray",
    opacity: float = 1.0,
    name: Optional[str] = None,
    show_legend: bool = False,
    show_init: bool = True,
    use_webgl: bool = False,
) -> go.Scatter:
    """Create a trace with line shapes.

    positional arguments:
      @ coords : (A list of) coordinate (x0, y0, x1, y1, x2, y2, x3, y3).

    positional arguments:
      @ text        : Texts for each data point.
      @ opacity     : Opacity of the rectangle.
      @ frame_width : Line width of the frame.
      @ frame_col   : Color of the frame.
      @ fill_col    : Color of the rectangle. To specify transparency, use "rgba()".
    """
    if not isinstance(coords[0], list):
        coords = [coords]
    return scatter(
        x=[
            x
            for _coords in coords
            for x in [x for x, y in _coords] + [_coords[0][0], None]
        ],
        y=[
            y
            for _coords in coords
            for y in [y for x, y in _coords] + [_coords[0][1], None]
        ],
        mode="lines",
        line_width=frame_width,
        col=frame_col,
        opacity=opacity,
        fill="toself" if fill_col is not None else None,
        fill_col=fill_col,
        name=name,
        show_legend=show_legend,
        show_init=show_init,
        use_webgl=use_webgl,
    )


def rects(
    coords: Union[Coord, List[Coord]],
    frame_width: float = 1,
    frame_col: Optional[str] = "black",
    fill_col: Optional[str] = "gray",
    opacity: float = 1.0,
    name: Optional[str] = None,
    show_legend: bool = False,
    show_init: bool = True,
    use_webgl: bool = False,
) -> go.Scatter:
    """Create a trace with rectangles.

    positional arguments:
      @ coords : (A list of) coordinate (x0, y0, x1, y1).

    positional arguments:
      @ text        : Texts for each data point.
      @ opacity     : Opacity of the rectangle.
      @ frame_width : Line width of the frame.
      @ frame_col   : Color of the frame.
      @ fill_col    : Color of the rectangle. To specify transparency, use "rgba()".
    """
    if not isinstance(coords, list):
        coords = [coords]
    coords = [[(x0, y0), (x0, y1), (x1, y1), (x1, y0)] for x0, y0, x1, y1 in coords]
    return closures(
        coords,
        frame_width,
        frame_col,
        fill_col,
        opacity,
        name,
        show_legend,
        show_init,
        use_webgl,
    )


def rects_shape(
    coords: Union[Coord, List[Coord]],
    xref: str = "x",
    yref: str = "y",
    fill_col: str = "grey",
    opacity: float = 1.0,
    frame_width: float = 1,
    frame_col: Optional[str] = "black",
    layer: str = "above",
) -> Dict:
    """Create a (non-interactive) rectangle object.

    positional arguments:
      @ coords : (A list of) coordinate (x0, y0, x1, y1).

    positional arguments:
      @ [x|y]ref    : Must be one of {'[x|y]', 'paper'}.
                      If "paper", values of `[x|y]0,1` must be within [0, 1]
                      and are interpreted as relative positions in the entire
                      [x|y]-axis.
      @ fill_col    : Color of the rectangle. For a transparent rectangle, use "rgba(0,0,0,0)".
      @ opacity     : Opacity of the rectangle.
      @ frame_width : Line width of the frame.
      @ frame_col   : Color of the frame.
      @ layer       : Drawing layer. Must be one of {'above', 'below'}.

    `xref` must be one of {"x" (default), "paper"}. "paper" means `x0` and `x1` indicate
    horizontal relative positions of the entire plot (values are in [0, 1]).
    (Same goes for `yref`.)
    `layer` must be one of {"above" (default), "below"}.
    """
    assert xref in ("x", "paper") and yref in (
        "y",
        "paper",
    ), "`[x|y]ref` must be '[x|y]' or 'paper'"
    assert layer in ("above", "below"), "`layer` must be 'above' or 'below'"

    def coord_to_shape(coord: Coord) -> Dict:
        x0, y0, x1, y1 = coord
        return dict(
            type="rect",
            xref=xref,
            yref=yref,
            x0=x0,
            y0=y0,
            x1=x1,
            y1=y1,
            fillcolor=fill_col,
            opacity=opacity,
            line=dict(color=frame_col, width=frame_width),
            layer=layer,
        )

    if not isinstance(coords, list):
        coords = [coords]

    return list(map(coord_to_shape, coords))
