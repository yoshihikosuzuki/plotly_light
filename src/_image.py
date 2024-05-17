from typing import Dict, Optional, Tuple

import PIL.Image
import plotly.graph_objects as go
from IPython.display import Image, display
from logzero import logger

from ._layout import layout


def image(
    in_fname: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    margin: Dict = dict(l=0, r=0, t=0, b=0),
    x_range: Optional[Tuple[int, int]] = None,
    y_range: Optional[Tuple[int, int]] = None,
    verbose: bool = False,
):
    img = PIL.Image.open(in_fname)
    iw, ih = img.size
    ar = ih / iw

    if x_range is not None:
        xb, xe = x_range
        if y_range is not None:
            yb, ye = y_range
        else:
            yb, ye = 0, (xe - xb) * ar
    else:
        if y_range is not None:
            yb, ye = y_range
            xb, xe = 0, (ye - yb) / ar
        else:
            xb, xe = 0, iw
            yb, ye = 0, ih

    if width is not None:
        if height is None:
            height = width * ar
    else:
        if height is not None:
            width = height / ar
        else:
            width, height = iw, ih

    if verbose:
        logger.info(
            f"plot = W {width:.1f} x H {height:.1f}, range = x[{xb:.1f}..{xe:.1f}] - y[{yb:.1f}..{ye:.1f}]"
        )

    fig = go.Figure(
        layout=layout(
            width=width,
            height=height,
            x_range=(xb, xe),
            y_range=(yb, ye),
            margin=margin,
        )
    )
    if x_range is None and y_range is None:
        fig.update_layout(
            xaxis=dict(showticklabels=False),
            yaxis=dict(showticklabels=False),
        )
    fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=xb,
            y=ye,
            sizex=xe - xb,
            sizey=ye - yb,
            sizing="stretch",
            layer="below",
        )
    )
    return fig


def show_image(
    fname: str,
    static: bool = False,
    width: Optional[int] = None,
    height: Optional[int] = None,
    margin: Dict = dict(l=0, r=0, t=0, b=0),
    x_range: Optional[Tuple[int, int]] = None,
    y_range: Optional[Tuple[int, int]] = None,
    verbose: bool = False,
) -> None:
    """Quick utility for plotting an image file in Jupyter Notebook.

    positional arguments:
      @ fname : Name of the image file.

    optional arguments:
      @ static         : If True, show the image as a non-interactive, static plot.
      @ width | height : Of the image.
    """
    if static:
        display(Image(fname, width=width, height=height))
    else:
        image(fname, width, height, margin, x_range, y_range, verbose).show()
