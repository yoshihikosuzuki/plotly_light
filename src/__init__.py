from ._histogram import make_hist
from ._scatter import make_scatter
from ._line import make_lines
from ._rectangle import make_rect
from ._layout import make_layout, merge_layout
from ._show import make_figure, show, show_image
from ._type import Traces
from ._config import set_default_layout, set_default_theme, set_default_renderer

# If running in an IPython environment, turn on the connected notebook mode


def _notebook_mode() -> None:
    import plotly.offline as py
    py.init_notebook_mode(connected=True)


def _set_custom_iframe_renderers() -> None:
    from os.path import basename
    import plotly.io as pio
    from plotly.io._base_renderers import IFrameRenderer
    from logzero import logger
    from uuid import uuid4
    import ipynb_path

    class MyIFrameRenderer(IFrameRenderer):
        """Custom renderer for `iframe` and `iframe_connected`, in which HTML file
        names of plots are unique and thus kept forever.
        """

        def build_filename(self):
            out_fname = f"{self.html_directory}/{uuid4()}.html"
            logger.debug(f"./{out_fname}")
            return out_fname

    nb_name = basename(ipynb_path.get())
    out_dir = f"{nb_name}.iframe_figures"
    pio.renderers["iframe"] = MyIFrameRenderer(config=pio._renderers.config,
                                               include_plotlyjs=True,
                                               html_directory=out_dir)
    pio.renderers["iframe_connected"] = MyIFrameRenderer(config=pio._renderers.config,
                                                         include_plotlyjs="cdn",
                                                         html_directory=out_dir)


try:
    get_ipython()
except NameError:
    pass
except Exception as e:
    print(e)
else:
    _notebook_mode()
    try:
        _set_custom_iframe_renderers()
    except Exception as e:
        pass
    else:
        set_default_renderer("iframe_connected")


# Set Plotly Light's default theme/layout

set_default_theme("plotly_white")
set_default_layout(make_layout(font="Arial",
                               font_col="black",
                               font_size_title=20,
                               font_size_axis_title=18,
                               font_size_axis_tick=15,
                               font_size_legend=15,
                               margin=dict(l=10, r=10, t=30, b=10)))
