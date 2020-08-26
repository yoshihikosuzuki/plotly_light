from typing import Union, Optional, List
import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
from .layout import make_layout


def show(traces: Union[BaseTraceType, List[BaseTraceType]],
         layout: Optional[go.Layout] = None,
         download_as: str = "svg",
         out_html: Optional[str] = None,
         embed_plotlyjs: bool = True):
    """Plot a figure in Jupyter Notebook.

    positional arguments:
      @ traces : A trace or list of traces.

    optional arguments:
      @ layout         : A layout object.
      @ download_as    : File format of the "Download plot" buttion in the plot.
      @ out_html       : Output the plot to an html file.
      @ embed_plotlyjs : If True, embed plotly.js codes (~3 MB) in `out_html`.
    """
    assert download_as in ("png", "jpeg", "svg"), \
        f"Unsupported output file type: {download_as}"
    fig = go.Figure(data=traces,
                    layout=layout if layout is not None else make_layout())
    fig.show(config=dict(toImageButtonOptions=dict(format=download_as)))
    if out_html is not None:
        fig.write_html(file=out_html,
                       include_plotlyjs=embed_plotlyjs)
