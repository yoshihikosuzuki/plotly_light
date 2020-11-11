from typing import Union, Optional, List
import plotly.graph_objects as go
from ._layout import make_layout
from ._type import Traces


def make_figure(traces: Traces,
                layout: Optional[go.Layout] = None) -> go.Figure:
    """Same as go.Figure(), just for compatibility.

    positional arguments:
      @ traces : A trace or list of traces.

    optional arguments:
      @ layout         : A layout object.
    """
    return go.Figure(data=traces,
                     layout=layout if layout is not None else make_layout())
