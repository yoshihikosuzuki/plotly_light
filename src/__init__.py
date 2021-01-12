from ._histogram import make_hist
from ._scatter import make_scatter
from ._line import make_lines
from ._rectangle import make_rect
from ._layout import make_layout, merge_layout
from ._figure import make_figure
from ._show import show, show_image
from ._type import Traces
from ._config import set_theme, set_renderer


try:
    get_ipython()
except NameError:
    pass
except Exception as e:
    print(e)
else:
    import plotly.offline as py
    py.init_notebook_mode(connected=True)

set_theme('simple_white')
