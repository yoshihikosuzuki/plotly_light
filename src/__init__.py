from ._histogram import make_hist
from ._bar import make_bar
from ._scatter import make_scatter
from ._line import make_lines
from ._rectangle import make_rect
from ._layout import make_layout, merge_layout
from ._show import make_figure, show, show_image
from ._type import Traces, BaseTraceType
from ._config import (set_default_layout,
                      update_default_layout,
                      set_default_theme,
                      set_default_renderer,
                      set_default_config)
from ._renderer import _set_custom_iframe_renderers
from ._crawl import _remove_unused_htmls
from ._theme import pl_layout


# If imported from an IPython environment, turn on the connected notebook mode.
# Moreover, if it is a Jupyter notebook, define and set a customized iframe renderer.
try:
    get_ipython()
except NameError:
    pass
except Exception as e:
    print(e)
else:
    import plotly.offline as py
    py.init_notebook_mode(connected=True)

    try:
        _set_custom_iframe_renderers()
    except Exception as e:
        pass
    else:
        set_default_renderer("iframe_connected")
        _remove_unused_htmls()


# Use custom default theme/layout/config
set_default_theme("simple_white")
set_default_layout(merge_layout(pl_layout,
                                make_layout(font="Arial",
                                            font_col="black",
                                            font_size=16,
                                            legend_border_col="black",
                                            margin=dict(l=10, r=10, t=50, b=10))))
set_default_config(dict(showTips=False,
                        displaylogo=False,
                        toImageButtonOptions=dict(format="svg")))
