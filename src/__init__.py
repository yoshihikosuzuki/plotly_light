from ._histogram import make_hist
from ._scatter import make_scatter
from ._line import make_lines
from ._rectangle import make_rect
from ._layout import make_layout, merge_layout
from ._show import make_figure, show, show_image
from ._type import Traces
from ._config import set_default_layout, set_default_theme, set_default_renderer


def _notebook_mode() -> None:
    import plotly.offline as py
    py.init_notebook_mode(connected=True)


try:
    get_ipython()
except NameError:
    pass
except Exception as e:
    print(e)
else:
    _notebook_mode()

set_default_theme("plotly_white")
set_default_layout(make_layout(font="Arial",
                               font_size_title=20,
                               font_size_axis_title=18,
                               font_size_axis_tick=15,
                               font_size_legend=15,
                               margin=dict(l=10, r=10, t=30, b=10)))
