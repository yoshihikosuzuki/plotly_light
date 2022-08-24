from typing import Any, Union, List, Sequence, Set
from plotly.basedatatypes import BaseTraceType

Traces = Union[BaseTraceType, List[BaseTraceType]]
DataSet = Union[Sequence, Set[Any]]
