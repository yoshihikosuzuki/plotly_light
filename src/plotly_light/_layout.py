from typing import Dict, List, Optional, Tuple, Union

import plotly.graph_objects as go

from . import default


def layout(
    # plot size
    width: Optional[int] = None,
    height: Optional[int] = None,
    size: Optional[int] = None,
    # plot range
    x_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
    y_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
    xy_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
    # overall font
    font: Optional[str] = None,
    font_col: Optional[str] = None,
    font_size: Optional[int] = None,
    # title
    title: Optional[str] = None,
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    x_titlefontsize: Optional[int] = None,
    y_titlefontsize: Optional[int] = None,
    xy_titlefontsize: Optional[int] = None,
    # bounding lines, zero lines, grids
    box: Optional[bool] = None,
    x_grid: Optional[bool] = None,
    y_grid: Optional[bool] = None,
    xy_grid: Optional[bool] = None,
    grid_col: Optional[str] = None,
    grid_width: Optional[float] = None,
    x_zeroline: Optional[bool] = None,
    y_zeroline: Optional[bool] = None,
    xy_zeroline: Optional[bool] = None,
    zeroline_col: Optional[str] = None,
    zeroline_width: Optional[float] = None,
    x_bounding_line: Optional[bool] = None,
    y_bounding_line: Optional[bool] = None,
    xy_bounding_line: Optional[bool] = None,
    bounding_line_col: Optional[str] = None,
    bounding_line_width: Optional[float] = None,
    x_mirror: Optional[Union[bool, str]] = None,
    y_mirror: Optional[Union[bool, str]] = None,
    xy_mirror: Optional[Union[bool, str]] = None,
    # axes
    anchor_axes: Optional[bool] = None,
    x_category: Optional[bool] = None,
    y_category: Optional[bool] = None,
    x_logscale: Optional[bool] = None,
    y_logscale: Optional[bool] = None,
    x_reversed: Optional[bool] = None,
    y_reversed: Optional[bool] = None,
    x_axis_hide: Optional[bool] = None,
    y_axis_hide: Optional[bool] = None,
    # axis ticks
    x_ticks: Optional[Union[str, bool]] = None,
    y_ticks: Optional[Union[str, bool]] = None,
    xy_ticks: Optional[Union[str, bool]] = None,
    x_dtick: Optional[int] = None,
    y_dtick: Optional[int] = None,
    xy_dtick: Optional[int] = None,
    x_ticks_minor: Optional[Union[str, bool]] = None,
    y_ticks_minor: Optional[Union[str, bool]] = None,
    xy_ticks_minor: Optional[Union[str, bool]] = None,
    x_nticks_minor: Optional[int] = None,
    y_nticks_minor: Optional[int] = None,
    xy_nticks_minor: Optional[int] = None,
    x_ticklabel: Optional[bool] = None,
    y_ticklabel: Optional[bool] = None,
    x_tickformat: Optional[str] = None,
    y_tickformat: Optional[str] = None,
    x_tickfontsize: Optional[int] = None,
    y_tickfontsize: Optional[int] = None,
    xy_ticksfontsize: Optional[int] = None,
    x_standoff: Optional[int] = None,
    y_standoff: Optional[int] = None,
    xy_standoff: Optional[int] = None,
    tick_col: Optional[str] = None,
    tick_len: Optional[float] = None,
    tick_width: Optional[float] = None,
    # legend
    show_legend: Optional[bool] = None,
    legend_horizontal: Optional[bool] = None,
    legend_coord: Optional[Tuple[Optional[float], Optional[float]]] = None,
    legend_border_col: Optional[str] = None,
    legend_border_width: Optional[int] = None,
    margin: Optional[Dict] = None,
    # shapes
    shapes: Optional[List[Dict]] = None,
    # bar plot
    barmode: Optional[str] = None,
    # interactive features
    hovermode: Optional[Union[str, bool]] = None,
) -> go.Layout:
    """Create a minimal Layout object.

    optional arguments:
      @ width                : Width of the plot.
      @ height               : Height of the plot.
      @ size                 : Both width and height of the plot.
      @ font                 : Font of characters in the plots.
      @ font_col             : Font color of charactoers in the plots.
      @ font_size_[title|axis_title|axis_tick|legend]
                             : Font size of title/x,y_title/x,y_tick/legend.
                               If None, the value is adaptively set based on `default.plot_size`
                               and `default.font_size`.
      @ title                : Title of the plot.
      @ [x|y]_title          : Title of [x|y]-axis of the plot.
      @ [x|y]_range          : Range on [x|y]-axis to be drawn in the plot.
      @ [x|y]_category       : Use categorical (string) labels for [x|y]-axis if True.
      @ [x|y]_logscale       : Use log scale for [x|y]-axis if True.
      @ [x|y]_grid           : Show grid on [x|y]-axis if True.
      @ [x|y]_zeroline       : Show zeroline on [x|y]-axis if True.
      @ [x|y]_reversed       : Reverse [x|y]-axis if True.
      @ [x|y]_axis_hide      : Hide [x|y]-axis if True.
      @ [x|y]_ticks          : {"" (or False; default), "outside" (or True), "inside"}.
      @ [x|y]_dtick          : Distance between two adjacent ticks.
      @ [x|y]_ticklabel      : Show tick labels of [x|y]-axis if True.
      @ [x|y]_tickformat     : e.g. ",.0f" (integer w/ commas), "%"
      @ [x|y]_standoff       : Size (in px) of the margin between tick labels and axis title.
      @ [x|y]_bounding_line  : Show line bewteen axis and plot if True.
      @ [x|y]_mirror         : {True, "ticks", False, "all", "allticks"}.
                               Show bounding line/ticks on the other side of the plot.
      @ anchor_axes          : Use same scale for both x/y axes.
      @ [grid|zeroline]_col  : Color of the grids and the zerolines.
      @ tick_[col|len|width] : Color/length/width of the ticks.
      @ bounding_line_[col|width]
                             : Color/width of the ticks.
      @ show_legend          : Show legend if True.
      @ legend_horizontal    : Shoe legend horizontally if True.
      @ legend_coord         : Relative coordinate (x, y) of the legend.
                               Default: (x, y) = (1.02, 1).
      @ legend_border_[col|width]
                             : Color/width for the borderlines of the legend box.
      @ margin               : Margin of the plot. Any number of keys can be specified.
                               Default: `dict(t=50, b=10, l=10, r=10, pad=0)`.
      @ shapes               : List of non-interactive shape objects.
      @ barmode              : {"group" (default), "stack", "overlay", "relative"}.
      @ hovermode            : {"closest" (default), "[x|y] [unified]", False}.
    """
    if size is not None:
        width = size
        height = size
    if width is None:
        width = default.plot_size
    if height is None:
        height = default.plot_size
    ratio = min(width, height) / default.plot_size

    if font_size is None:
        font_size = default.font_size * ratio
    if grid_width is None:
        grid_width = default.grid_width * ratio
    if tick_len is None:
        tick_len = default.tick_len * ratio
    if tick_width is None:
        tick_width = default.tick_width * ratio
    if bounding_line_width is None:
        bounding_line_width = default.bounding_line_width * ratio
    if zeroline_width is None:
        zeroline_width = default.bounding_line_width * ratio
    if legend_border_width is None:
        legend_border_width = default.bounding_line_width * ratio

    if box is not None:
        if x_bounding_line is None:
            x_bounding_line = box
        if y_bounding_line is None:
            y_bounding_line = box
        if x_mirror is None:
            x_mirror = box
        if y_mirror is None:
            y_mirror = box
        if x_ticks is None:
            x_ticks = box
        if y_ticks is None:
            y_ticks = box

    if xy_range is not None:
        x_range = xy_range
        y_range = xy_range
    if xy_titlefontsize is not None:
        x_titlefontsize = xy_titlefontsize
        y_titlefontsize = xy_titlefontsize
    if xy_grid is not None:
        x_grid = xy_grid
        y_grid = xy_grid
    if xy_zeroline is not None:
        x_zeroline = xy_zeroline
        y_zeroline = xy_zeroline
    if xy_bounding_line is not None:
        x_bounding_line = xy_bounding_line
        y_bounding_line = xy_bounding_line
    if xy_mirror is not None:
        x_mirror = xy_mirror
        y_mirror = xy_mirror
    if xy_ticks is not None:
        x_ticks = xy_ticks
        y_ticks = xy_ticks
    if xy_ticks_minor is not None:
        x_ticks_minor = xy_ticks_minor
        y_ticks_minor = xy_ticks_minor
    if xy_nticks_minor is not None:
        x_nticks_minor = xy_nticks_minor
        y_nticks_minor = xy_nticks_minor
    if xy_dtick is not None:
        x_dtick = xy_dtick
        y_dtick = xy_dtick
    if xy_ticksfontsize is not None:
        x_tickfontsize = xy_ticksfontsize
        y_tickfontsize = xy_ticksfontsize
    if xy_standoff is not None:
        x_standoff = xy_standoff
        y_standoff = xy_standoff

    return go.Layout(
        width=width,
        height=height,
        font=dict(family=font, size=font_size, color=font_col),
        title=dict(text=title),
        xaxis=dict(
            visible=not x_axis_hide,
            title=dict(
                text=x_title, font=dict(size=x_titlefontsize), standoff=x_standoff
            ),
            type=(
                "category"
                if x_category is True
                else "log" if x_logscale is True else None
            ),
            range=x_range,
            autorange="reversed" if x_reversed is True else None,
            ticks="outside" if x_ticks is True else "" if x_ticks is False else x_ticks,
            minor=dict(
                ticks=(
                    "outside"
                    if x_ticks_minor is True
                    else "" if x_ticks_minor is False else x_ticks_minor
                ),
                nticks=None if x_nticks_minor is None else x_nticks_minor + 1,
            ),
            dtick=x_dtick,
            showticklabels=x_ticklabel,
            tickformat=x_tickformat,
            tickfont=dict(size=x_tickfontsize),
            tickcolor=tick_col,
            ticklen=tick_len,
            tickwidth=tick_width,
            showgrid=x_grid,
            gridcolor=grid_col,
            gridwidth=grid_width,
            zeroline=x_zeroline,
            zerolinecolor=zeroline_col,
            zerolinewidth=zeroline_width,
            showline=x_bounding_line,
            linecolor=bounding_line_col,
            linewidth=bounding_line_width,
            mirror=x_mirror,
        ),
        yaxis=dict(
            visible=not y_axis_hide,
            title=dict(
                text=y_title, font=dict(size=y_titlefontsize), standoff=y_standoff
            ),
            type=(
                "category"
                if y_category is True
                else "log" if y_logscale is True else None
            ),
            range=y_range,
            autorange="reversed" if y_reversed is True else None,
            scaleanchor="x" if anchor_axes is True else None,
            ticks="outside" if y_ticks is True else "" if y_ticks is False else y_ticks,
            minor=dict(
                ticks=(
                    "outside"
                    if y_ticks_minor is True
                    else "" if y_ticks_minor is False else y_ticks_minor
                ),
                nticks=None if y_nticks_minor is None else y_nticks_minor + 1,
            ),
            dtick=y_dtick,
            showticklabels=y_ticklabel,
            tickformat=y_tickformat,
            tickfont=dict(size=y_tickfontsize),
            tickcolor=tick_col,
            ticklen=tick_len,
            tickwidth=tick_width,
            showgrid=y_grid,
            gridcolor=grid_col,
            gridwidth=grid_width,
            zeroline=y_zeroline,
            zerolinecolor=zeroline_col,
            zerolinewidth=zeroline_width,
            showline=y_bounding_line,
            linecolor=bounding_line_col,
            linewidth=bounding_line_width,
            mirror=y_mirror,
        ),
        showlegend=show_legend,
        legend=dict(
            orientation="h" if legend_horizontal else None,
            bordercolor=legend_border_col,
            borderwidth=legend_border_width,
            x=None if legend_coord is None else legend_coord[0],
            y=None if legend_coord is None else legend_coord[1],
        ),
        margin=margin,
        shapes=shapes,
        barmode=barmode,
        hovermode=hovermode,
    )


def merge_layout(base_layout, *layouts) -> go.Layout:
    """Merge multiple layouts. The `base_layout` is iteratively updated by each
    of the other layouts in the order of arguments.
    """
    if not isinstance(base_layout, go.Layout):
        base_layout = layout().update(base_layout)
    for _layout in layouts:
        base_layout = base_layout.update(_layout)
    return base_layout
