from typing import Optional, Tuple, List, Dict
import plotly.graph_objects as go


def make_layout(width: Optional[int] = None,
                height: Optional[int] = None,
                font: str = "Arial",
                font_size_title: int = 20,
                font_size_axis_title: int = 18,
                font_size_axis_tick: int = 15,
                font_size_legend: int = 15,
                title: Optional[str] = None,
                x_title: Optional[str] = None,
                y_title: Optional[str] = None,
                x_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
                y_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
                x_grid: bool = True,
                y_grid: bool = True,
                x_zeroline: bool = True,
                y_zeroline: bool = True,
                x_reversed: bool = False,
                y_reversed: bool = False,
                x_ticklabel: bool = True,
                y_ticklabel: bool = True,
                anchor_axes: bool = False,
                margin: Dict = dict(l=10, r=10, t=30, b=10),
                shapes: Optional[List[Dict]] = None) -> go.Layout:
    """Create a simple Layout object.

    optional arguments:
      @ width           : Width of the plot.
      @ height          : Height of the plot.
      @ font            : Font of (axis) titles.
      @ font_size_[title|axis_title|axis_tick|legend]
                        : Font size of title/x,y_title/x,y_tick/legend.
      @ title           : Title of the plot.
      @ [x|y]_title     : Title of [x|y]-axis of the plot.
      @ [x|y]_range     : Range on [x|y]-axis to be drawn in the plot.
      @ [x|y]_grid      : Show grid on [x|y]-axis if True.
      @ [x|y]_zeroline  : Show zeroline on [x|y]-axis if True.
      @ [x|y]_reversed  : Reverse [x|y]-axis if True.
      @ [x|y]_ticklabel : Show tick labels of [x|y]-axis if True.
      @ anchor_axes     : Use same scale for both x/y axes.
      @ margin          : Margin of the plot.
                          Default: `dict(l=80, r=80, t=100, b=80)`.
      @ shapes          : List of non-interactive shape objects.
    """
    return go.Layout(
        width=width,
        height=height,
        hovermode="closest",
        title=dict(text=title,
                   font=dict(family=font,
                             size=font_size_title,
                             color="black")),
        xaxis=dict(title=dict(text=x_title,
                              font=dict(family=font,
                                        size=font_size_axis_title,
                                        color="black")),
                   tickfont=dict(family="Arial",
                                 size=font_size_axis_tick,
                                 color="black"),
                   showgrid=x_grid,
                   zeroline=x_zeroline,
                   showticklabels=x_ticklabel,
                   range=x_range,
                   autorange="reversed" if x_reversed else None),
        yaxis=dict(title=dict(text=y_title,
                              font=dict(family=font,
                                        size=font_size_axis_title,
                                        color="black")),
                   tickfont=dict(family="Arial",
                                 size=font_size_axis_tick,
                                 color="black"),
                   showgrid=y_grid,
                   zeroline=y_zeroline,
                   showticklabels=y_ticklabel,
                   range=y_range,
                   autorange="reversed" if y_reversed else None,
                   scaleanchor="x" if anchor_axes else None),
        legend=dict(font=dict(family=font,
                              size=font_size_legend,
                              color="black")),
        margin=margin,
        shapes=shapes)
