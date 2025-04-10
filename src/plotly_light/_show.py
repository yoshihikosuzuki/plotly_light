from math import sqrt
from typing import Dict, Optional, Sequence, Union

import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
from plotly.subplots import make_subplots

from . import _layout as pll
from . import default
from ._type import Traces


def figure(traces: Traces, layout: Optional[go.Layout] = None) -> go.Figure:
    """Same as go.Figure(), just for compatibility."""
    return go.Figure(data=traces, layout=layout)


def figure_mult(
    figs: Sequence[Union[BaseTraceType, go.Figure]],
    layout: Optional[go.Layout] = None,
    n_col: int = 2,
    row_heights: Optional[Sequence[float]] = None,
    col_widths: Optional[Sequence[float]] = None,
    horizontal_spacing: Optional[float] = 0.1,
    vertical_spacing: Optional[float] = 0.2,
    shared_xaxes: Union[bool, str] = False,
    shared_yaxes: Union[bool, str] = False,
) -> go.Figure:
    """Make a figure object with multiple sub-figures.

    positional arguments:
      @ figs : List of Trace or Figure objects. If an element is a Figure object,
               its layout is used for that subplot.

    optional arguments:
      @ layout           : A layout object for the overall figure.
      @ n_col            : Number of columns of plots. Number of rows is automatically determined.
      @ [row_heights|col_widths]
                         : List of relative heights/widths of each row/column.
      @ [horizontal|vertical]_spacing
                         : Size of spaces between subplots. Must be in [0, 1].
                           Default: horizontal = 0.1 / #cols, vertical = 0.2 / #rows.
      @ shared_[x|y]axes : Must be boolean or one of {"columns", "rows", "all"}.
    """
    N = len(figs)
    n_row = N // n_col + (0 if N % n_col == 0 else 1)

    # Decompose Figure (or Trace) into Traces & Layout
    sub_tracess, sub_layouts = zip(
        *[
            (
                (fig.data, fig.layout)
                if isinstance(fig, go.Figure)
                else ((fig,), pll.layout())
            )
            for fig in figs
        ]
    )
    sub_titles = [l.title.text for l in sub_layouts]
    if all([x is None for x in sub_titles]):
        sub_titles = None

    # Make entire figure, add each traces & layout, and add overall layout
    fig = make_subplots(
        rows=n_row,
        cols=n_col,
        row_heights=row_heights,
        column_widths=col_widths,
        shared_xaxes=shared_xaxes,
        shared_yaxes=shared_yaxes,
        horizontal_spacing=horizontal_spacing,
        vertical_spacing=vertical_spacing,
        subplot_titles=sub_titles,
    )

    for i in range(n_row):
        for j in range(1, n_col + 1):
            if i * n_col + j > N:
                continue
            idx = i * n_col + j - 1
            sub_traces = sub_tracess[idx]
            for sub_trace in sub_traces:
                fig.append_trace(sub_trace, row=i + 1, col=j)
            l = sub_layouts[idx]
            fig.update_xaxes(**l.xaxis.to_plotly_json(), row=i + 1, col=j)
            fig.update_yaxes(**l.yaxis.to_plotly_json(), row=i + 1, col=j)

            # Add images if exist
            if "images" in l:
                fig.layout.images = tuple(
                    list(fig.layout.images)
                    + list(
                        map(
                            lambda d: d.update(
                                {"xref": f"x{idx + 1}", "yref": f"y{idx + 1}"}
                            ),
                            l.images,
                        )
                    )
                )
    fig.update_layout(margin=dict(t=70, l=40))
    fig.update_layout(layout)

    return fig


def show(
    traces: Union[Traces, go.Figure],
    layout: Optional[go.Layout] = None,
    out_image: Optional[str] = None,
    config: Optional[Dict] = None,
    embed_plotlyjs: bool = True,
    no_plot: bool = False,
) -> None:
    """Plot a figure in Jupyter Notebook.

    positional arguments:
      @ traces : A trace, list of traces, or a Figure object.

    optional arguments:
      @ layout         : A layout object.
      @ out_image      : Image/HTML file name(s) to which the plot is output.
                         The format is e.g.:
                           - `out.pdf` for single output
                           - `out.{svg,pdf,html}` for multiple outputs
                         .[png|jpeg|svg|pdf|eps|html] are supported.
      @ embed_plotlyjs : If True, embed plotly.js codes (~3 MB) in the output HTML file.
      @ no_plot        : If True, do not draw a plot in an interactive environment.
    """
    # Make a figure object if needed
    if isinstance(traces, go.Figure):
        fig = traces
        if layout is None:
            layout = pll.layout()
        if layout is not None:
            fig.layout = pll.merge_layout(fig.layout, layout)
    else:
        fig = figure(traces, layout)

    # Prep config
    _config = default.config
    if config is not None:
        _config.update(config)

    # Determine the scale of the output image`
    if fig.layout.width is None:
        fig.layout.width = default.plot_size
    if fig.layout.height is None:
        fig.layout.height = default.plot_size
    scale = sqrt(
        ((default.dpi * default.plot_inch) ** 2)
        / (fig.layout.width * fig.layout.height)
    )
    # Output image(s)
    if out_image is not None:
        if out_image.endswith("}"):
            # multiple output formats
            data = out_image[:-1].split("{")
            assert len(data) == 2, f"Invalid format: {out_image}"
            prefix = data[0]
            exts = data[1].split(",")
            out_fnames = [f"{prefix}{ext}" for ext in exts]
        else:
            # single output formats
            out_fnames = [out_image]

        for out_fname in out_fnames:
            if out_fname.endswith(".html"):
                fig.write_html(
                    file=out_fname, config=config, include_plotlyjs=embed_plotlyjs
                )
            else:
                fig.write_image(out_fname, scale=scale)

    # Show plot
    if not no_plot:
        fig.show(config=_config)


def show_mult(
    figs: Sequence[Union[BaseTraceType, go.Figure]],
    layout: Optional[go.Layout] = None,
    config: Optional[Dict] = None,
    n_col: int = 2,
    row_heights: Optional[Sequence[float]] = None,
    col_widths: Optional[Sequence[float]] = None,
    horizontal_spacing: Optional[float] = 0.1,
    vertical_spacing: Optional[float] = 0.2,
    shared_xaxes: Union[bool, str] = False,
    shared_yaxes: Union[bool, str] = False,
    out_image: Optional[str] = None,
    embed_plotlyjs: bool = True,
    no_plot: bool = False,
) -> None:
    """Plot a figure with multiple subplots in Jupyter Notebook.

    positional arguments:
      @ figs : List of Trace or Figure objects. If an element is a Figure object,
               its layout is used for that subplot.

    optional arguments:
      @ layout           : A layout object for the overall figure.
      @ n_col            : Number of columns of plots. Number of rows is automatically determined.
      @ [row_heights|col_widths]
                         : List of relative heights/widths of each row/column.
      @ [horizontal|vertical]_spacing:
                         : Size of spaces between subplots. Must be in [0, 1].
                           Default: horizontal = 0.1 / #cols, vertical = 0.2 / #rows.
      @ shared_[x|y]axes : Must be boolean or one of {"columns", "rows", "all"}.
      @ out_image        : Image/HTML file name(s) to which the plot is output.
                           The format is:
                             - `out.pdf` for single output
                             - `out.{svg,pdf,html}` for multiple outputs
                           .[png|jpeg|svg|pdf|eps|html] are supported.
      @ embed_plotlyjs   : If True, embed plotly.js codes (~3 MB) in the output HTML file.
      @ no_plot        : If True, do not draw a plot in an interactive environment.
    """
    fig = figure_mult(
        figs,
        layout,
        n_col,
        row_heights,
        col_widths,
        horizontal_spacing,
        vertical_spacing,
        shared_xaxes,
        shared_yaxes,
    )

    show(
        fig,
        out_image=out_image,
        config=config,
        embed_plotlyjs=embed_plotlyjs,
        no_plot=no_plot,
    )
