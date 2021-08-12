from typing import Union, Optional, Tuple, List, Dict
import plotly.graph_objects as go


def make_layout(width: Optional[int] = None,
                height: Optional[int] = None,
                font: Optional[str] = None,
                font_col: Optional[str] = None,
                font_size: Optional[int] = None,
                title: Optional[str] = None,
                x_title: Optional[str] = None,
                y_title: Optional[str] = None,
                x_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
                y_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
                x_logscale: Optional[bool] = None,
                y_logscale: Optional[bool] = None,
                x_grid: Optional[bool] = None,
                y_grid: Optional[bool] = None,
                x_zeroline: Optional[bool] = None,
                y_zeroline: Optional[bool] = None,
                x_reversed: Optional[bool] = None,
                y_reversed: Optional[bool] = None,
                x_ticks: Optional[str] = None,
                y_ticks: Optional[str] = None,
                x_dtick: Optional[int] = None,
                y_dtick: Optional[int] = None,
                x_ticklabel: Optional[bool] = None,
                y_ticklabel: Optional[bool] = None,
                anchor_axes: Optional[bool] = None,
                legend_x: Optional[float] = None,
                legend_y: Optional[float] = None,
                legend_border_col: Optional[str] = None,
                legend_border_width: Optional[int] = None,
                margin: Optional[Dict] = None,
                shapes: Optional[List[Dict]] = None,
                barmode: Optional[str] = None,
                hovermode: Optional[Union[str, bool]] = None) -> go.Layout:
    """Create a minimal Layout object.

    optional arguments:
      @ width           : Width of the plot.
      @ height          : Height of the plot.
      @ font            : Font of characters in the plots.
      @ font_col        : Font color of charactoers in the plots.
      @ font_size_[title|axis_title|axis_tick|legend]
                        : Font size of title/x,y_title/x,y_tick/legend.
      @ title           : Title of the plot.
      @ [x|y]_title     : Title of [x|y]-axis of the plot.
      @ [x|y]_range     : Range on [x|y]-axis to be drawn in the plot.
      @ [x|y]_grid      : Show grid on [x|y]-axis if True.
      @ [x|y]_zeroline  : Show zeroline on [x|y]-axis if True.
      @ [x|y]_reversed  : Reverse [x|y]-axis if True.
      @ [x|y]_ticks     : {"" (default), "outside", "inside"}.
      @ [x|y]_dtick     : Distance between two adjacent ticks.
      @ [x|y]_ticklabel : Show tick labels of [x|y]-axis if True.
      @ anchor_axes     : Use same scale for both x/y axes.
      @ legend_[x|y]    : Relative position of the legend.
                          (x, y) = (1.02, 1) by default.
      @ legend_border_[col|width]
                        : Color/width for the borderlines of the legend box.
      @ margin          : Margin of the plot.
                          Default: `dict(l=80, r=80, t=100, b=80)`.
      @ shapes          : List of non-interactive shape objects.
      @ barmode         : {"group" (default), "stack", "overlay", "relative"}.
      @ hovermode       : {"closest" (default), "[x|y] [unified]", False}.
    """

    layout = go.Layout(width=width,
                       height=height,
                       hovermode=hovermode,
                       font=dict(family=font,
                                 size=font_size,
                                 color=font_col),
                       title=dict(text=title),
                       xaxis=dict(title=dict(text=x_title),
                                  showgrid=x_grid,
                                  zeroline=x_zeroline,
                                  showticklabels=x_ticklabel,
                                  range=x_range,
                                  ticks=x_ticks,
                                  dtick=x_dtick),
                       yaxis=dict(title=dict(text=y_title),
                                  showgrid=y_grid,
                                  zeroline=y_zeroline,
                                  showticklabels=y_ticklabel,
                                  range=y_range,
                                  ticks=y_ticks,
                                  dtick=y_dtick),
                       legend=dict(bordercolor=legend_border_col,
                                   borderwidth=legend_border_width,
                                   x=legend_x,
                                   y=legend_y),
                       margin=margin,
                       shapes=shapes,
                       barmode=barmode)
    if x_logscale:
        layout.xaxis.type = "log"
    if x_reversed:
        layout.xaxis.autorange = "reversed"
    if y_logscale:
        layout.yaxis.type = "log"
    if y_reversed:
        layout.yaxis.autorange = "reversed"
    if anchor_axes:
        layout.yaxis.scaleanchor = "x"
    return layout


def merge_layout(layout1: Union[go.Layout, Dict, None],
                 layout2: Union[go.Layout, Dict, None],
                 overwrite: bool = True) -> go.Layout:
    """Merge two layouts.

    positional arguments:
      @ layout[1|2] : Layout object or dictionary.

    optional arguments:
      @ overwrite : If True, values of layout2 are used for shared keys.
    """
    return (layout1 if layout2 is None
            else layout2 if layout1 is None
            else ((layout1 if isinstance(layout1, go.Layout)
                   else make_layout().update(layout1, overwrite=True))
                  .update(layout2, overwrite=overwrite)))
