from typing import Union, Optional, List
import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
from ._layout import make_layout


def make_figure(traces: Union[BaseTraceType, List[BaseTraceType]],
                layout: Optional[go.Layout] = None):
    """Same as go.Figure(), just for compatibility.

    positional arguments:
      @ traces : A trace or list of traces.

    optional arguments:
      @ layout         : A layout object.
    """
    return go.Figure(data=traces,
                     layout=layout if layout is not None else make_layout())
