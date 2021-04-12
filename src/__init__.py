from ._histogram import make_hist
from ._bar import make_bar
from ._scatter import make_scatter
from ._line import make_lines
from ._rectangle import make_rect
from ._layout import make_layout, merge_layout
from ._show import make_figure, show, show_image
from ._type import Traces, BaseTraceType
from ._config import (set_default_layout,
                      set_default_theme,
                      set_default_renderer,
                      set_default_config)


def _notebook_mode() -> None:
    import plotly.offline as py
    py.init_notebook_mode(connected=True)


def _set_custom_iframe_renderers() -> None:
    import plotly.io as pio
    from ._renderer import MyIFrameRenderer
    pio.renderers["iframe"] = MyIFrameRenderer(config=pio._renderers.config,
                                               include_plotlyjs=True)
    pio.renderers["iframe_connected"] = MyIFrameRenderer(config=pio._renderers.config,
                                                         include_plotlyjs="cdn")


try:
    get_ipython()
except NameError:
    pass
except Exception as e:
    print(e)
else:
    # If running in an IPython environment, turn on the connected notebook mode
    _notebook_mode()
    try:
        # Moreover, if running in a Jupyter notebook, use customized iframe renderer
        _set_custom_iframe_renderers()
    except Exception as e:
        pass
    else:
        set_default_renderer("iframe_connected")


# Use custom default theme/layout/config
set_default_theme("plotly_white")
set_default_layout(make_layout(font="Arial",
                               font_col="black",
                               font_size=16,
                               legend_border_col="black",
                               margin=dict(l=10, r=10, t=50, b=10)))
set_default_config(dict(showTips=False,
                        displaylogo=False,
                        toImageButtonOptions=dict(format="svg")))
