from ._histogram import hist
from ._bar import bar
from ._scatter import scatter
from ._line import lines
from ._rectangle import rect
from ._venn import venn
from ._layout import layout, merge_layout
from ._show import figure, show, show_image
from ._type import Traces, BaseTraceType
from ._config import (set_default_layout,
                      update_default_layout,
                      set_default_theme,
                      set_default_renderer,
                      set_default_config)
from ._renderer import _set_custom_iframe_renderers
from ._crawl import _remove_unused_htmls
from ._theme import pl_layout

# Function aliases for backward compatibility and ease of search
make_hist = hist
make_bar = bar
make_scatter = scatter
make_lines = lines
make_rect = rect
make_venn = venn
make_layout = layout
make_figure = figure


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
set_default_layout(pl_layout)
set_default_config(dict(showTips=False,
                        displaylogo=False,
                        modeBarButtonsToAdd=["hoverclosest",
                                             "hovercompare"],
                        toImageButtonOptions=dict(format="svg")))
