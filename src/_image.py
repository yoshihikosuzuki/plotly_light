from typing import Dict, Optional

import plotly.express as px
import plotly.graph_objects as go
from IPython.display import Image, display
from skimage import io


def image(fname: str,
          width: Optional[int] = None,
          height: Optional[int] = None,
          margin: Dict = dict(l=0, r=0, t=0, b=0)) -> go.Figure:
    """Return an interactive figure object of an image loaded from a file.

    positional arguments:
      @ fname : Name of the image file.

    optional arguments:
      @ width | height : Of the image.
    """
    fig = px.imshow(io.imread(fname))
    fig.update_layout(width=width,
                      height=height,
                      xaxis=dict(showgrid=False,
                                 zeroline=False,
                                 showticklabels=False,
                                 domain=None),
                      yaxis=dict(showgrid=False,
                                 zeroline=False,
                                 showticklabels=False,
                                 domain=None),
                      margin=margin)
    return fig


def show_image(fname: str,
               interactive: bool = False,
               width: Optional[int] = None,
               height: Optional[int] = None,
               margin: Dict = dict(l=0, r=0, t=0, b=0)) -> None:
    """Quick utility for plotting an image file in Jupyter Notebook.

    positional arguments:
      @ fname : Name of the image file.

    optional arguments:
      @ interactive    : If True, plot an interective plot.
      @ width | height : Of the image.
    """
    if not interactive:
        display(Image(fname, width=width, height=height))
    else:
        image(fname, width, height, margin).show()
