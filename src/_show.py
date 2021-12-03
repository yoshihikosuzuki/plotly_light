from typing import Union, Optional, Dict
from IPython.display import Image, display
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from skimage import io
from ._layout import merge_layout
from ._type import Traces


def figure(traces: Traces,
           layout: Optional[go.Layout] = None) -> go.Figure:
    """Same as go.Figure(), just for compatibility.

    positional arguments:
      @ traces : A trace or list of traces.

    optional arguments:
      @ layout         : A layout object.
    """
    return go.Figure(data=traces, layout=layout)


def show(traces: Union[Traces, go.Figure],
         layout: Optional[go.Layout] = None,
         out_image: Optional[str] = None,
         out_html: Optional[str] = None,
         embed_plotlyjs: bool = True,
         do_not_display: bool = False) -> None:
    """Plot a figure in Jupyter Notebook.

    positional arguments:
      @ traces : A trace, list of traces, or a Figure object.

    optional arguments:
      @ layout         : A layout object.
      @ out_html       : HTML file name to which the plot is output.
      @ out_image      : Image file name to which the plot is output.
                         .[png|jpeg|svg|pdf|eps] are supported.
      @ embed_plotlyjs : If True, embed plotly.js codes (~3 MB) in `out_html`.
      @ do_not_display : If True, do not draw the plot.
    """
    if isinstance(traces, go.Figure):
        fig = traces
        if layout is not None:
            fig.layout = merge_layout(fig.layout, layout)
    else:
        fig = figure(traces, layout)
    if not do_not_display:
        fig.show()
    if out_image is not None:
        fig.write_image(out_image)
    if out_html is not None:
        fig.write_html(file=out_html,
                       include_plotlyjs=embed_plotlyjs)


def show_mult(traces: Union[Traces, go.Figure],
              layout: Optional[go.Layout] = None,
              n_col: int = 2,
              out_image: Optional[str] = None,
              out_html: Optional[str] = None,
              embed_plotlyjs: bool = True,
              do_not_display: bool = False) -> None:
    """Plot a figure with multiple subplots in Jupyter Notebook.

    positional arguments:
      @ traces : A trace, list of traces, or a Figure object.

    optional arguments:
      @ layout         : A layout object.
      @ n_col          : Number of columns of plots. Number of rows is automatically determined.
      @ out_html       : HTML file name to which the plot is output.
      @ out_image      : Image file name to which the plot is output.
                         .[png|jpeg|svg|pdf|eps] are supported.
      @ embed_plotlyjs : If True, embed plotly.js codes (~3 MB) in `out_html`.
      @ do_not_display : If True, do not draw the plot.
    """
    def infer_trace_type(trace):
        return {"type": "xy"}

    n_row = len(traces) // n_col + (0 if len(traces) % n_col == 0 else 1)
    trace_types = [[infer_trace_type(traces[i * n_col + j]) if i * n_col + j < len(traces) else {}
                    for j in range(n_col)] for i in range(n_row)]
    fig = make_subplots(rows=n_row, cols=n_col, specs=trace_types)
    for i in range(n_row):
        for j in range(1, n_col + 1):
            if i * n_col + j > len(traces):
                continue
            fig.add_trace(traces[i * n_col + j - 1], row=i + 1, col=j)
    fig.update_layout(layout)
    if not do_not_display:
        fig.show()
    if out_image is not None:
        fig.write_image(out_image)
    if out_html is not None:
        fig.write_html(file=out_html,
                       include_plotlyjs=embed_plotlyjs)


def show_image(fname: str,
               interactive: bool = False,
               width: Optional[int] = None,
               height: Optional[int] = None,
               margin: Dict = dict(l=0, r=0, t=0, b=0)) -> None:
    """Plot an image file in Jupyter Notebook.

    positional arguments:
      @ fname : Name of the image file.

    optional arguments:
      @ interactive : If True, plot an interective (but very large) plot.
      @ width  : Of the image.
      @ height : Of the image.
    """
    if not interactive:
        display(Image(fname, width=width, height=height))
    else:
        fig = px.imshow(io.imread(fname))
        fig.update_layout(width=width,
                          height=height,
                          xaxis=dict(showgrid=False,
                                     zeroline=False,
                                     showticklabels=False),
                          yaxis=dict(showgrid=False,
                                     zeroline=False,
                                     showticklabels=False),
                          margin=margin)
        fig.show()
