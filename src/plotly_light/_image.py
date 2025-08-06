from typing import Optional, Tuple

import PIL.Image
import plotly.graph_objects as go
from IPython.display import Image, display
from logzero import logger

from . import _layout as pll
from . import default
from ._show import show


def image(
    in_fname: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    min_size: Optional[int] = 100,
    axis_label_size: Optional[int] = 100,
    x_range: Optional[Tuple[int, int]] = None,
    y_range: Optional[Tuple[int, int]] = None,
    layer: str = "above",
    opacity: Optional[float] = None,
    layout: go.Layout = None,
    autoscale_font_by: str = None,
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

    if width is None and height is None:
        width = default.plot_size - axis_label_size
        height = default.plot_size - axis_label_size
    if width is not None:
        width -= axis_label_size
        if height is not None:
            height -= axis_label_size
            width, height = min(width, height / ar), min(height, width * ar)
        else:
            height = width * ar
    else:  # height is not None
        height -= axis_label_size
        width = height / ar

    width += axis_label_size
    height += axis_label_size

    if width < min_size:
        logger.warning(
            f"Width ({width:.1f}) is too small. Setting the minimum value, {min_size}."
        )
        width = min_size
    if height < min_size:
        logger.warning(
            f"Height ({height:.1f}) is too small. Setting the minimum value, {min_size}."
        )
        height = min_size

    if verbose:
        logger.info(
            f"plot = W {width:.1f} x H {height:.1f}, range = x[{xb:.1f}..{xe:.1f}] - y[{yb:.1f}..{ye:.1f}]"
        )

    fig = go.Figure(
        layout=pll.merge_layout(
            # default layout options with the lowest priority
            pll.layout(
                width=width,
                height=height,
                box=False,
                anchor_axes=True,
                x_ticklabel=x_range is not None,
                y_ticklabel=y_range is not None,
                margin=dict(l=5, r=5, t=5, b=5),
            ),
            # user-defined layout options with middle priority
            layout,
            # default layout options with highest priority
            pll.layout(
                x_range=(xb, xe),
                y_range=(yb, ye),
            ),
        )
    )

    # Force to plot only the domain specified by `x_range` and `y_range`
    fig.update_xaxes(constrain='domain')
    fig.update_yaxes(constrain='domain')
    
    fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=xb,
            y=ye,
            sizex=xe - xb,
            sizey=yb - ye,
            sizing="stretch",
            layer=layer,
            opacity=opacity,
        )
    )
    pll.autoscale_plot_font_sizes(fig.layout, by=autoscale_font_by)

    return fig


def show_image(
    fname: str,
    static: bool = False,
    width: Optional[int] = None,
    height: Optional[int] = None,
    x_range: Optional[Tuple[int, int]] = None,
    y_range: Optional[Tuple[int, int]] = None,
    layer: str = "above",
    opacity: Optional[float] = None,
    layout: go.Layout = None,
    autoscale_font_by: str = None,
    return_fig: bool = False,
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
        assert not return_fig, "`return_fig` must not be True for static image"
        display(Image(fname, width=width, height=height))
        return

    fig = image(
        in_fname=fname,
        width=width,
        height=height,
        x_range=x_range,
        y_range=y_range,
        layer=layer,
        opacity=opacity,
        layout=layout,
        autoscale_font_by=autoscale_font_by,
        verbose=verbose,
    )

    if return_fig:
        return fig

    show(fig)
