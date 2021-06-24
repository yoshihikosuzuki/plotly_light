from typing import Any, Dict
import plotly.io as pio
import plotly.graph_objects as go
from ._layout import merge_layout


default_theme = pio.templates.default
default_layout = None


def _set_default_template() -> None:
    """Set the combination of the user-defined theme and layout as the default
    template.
    """
    global default_theme, default_layout
    pio.templates["plotly_light"] = pio.templates.merge_templates(
        pio.templates[default_theme],
        go.layout.Template(layout=default_layout))
    pio.templates.default = "plotly_light"


def set_default_theme(theme_name: str,
                      keep_layout: bool = True) -> None:
    """Change plotly's default theme.

    positional_arguments:
      @ theme_name : A plotly theme name like:
                      {"ggplot2",
                       "seaborn",
                       "simple_white",
                       "plotly",
                       "plotly_white",
                       "plotly_dark",
                       "none"}

    optional arguments:
      @ keep_layout : If True, overwrite the theme's layout with the 
                             default layout set by `set_default_layout()`.
    """
    global default_theme
    pio.templates.default = default_theme = theme_name
    if keep_layout and default_layout is not None:
        _set_default_template()


def set_default_layout(layout: go.Layout) -> None:
    """Change the default layout for plots.

    positional arguments:
      @ layout : The layout object.
    """
    global default_layout
    default_layout = layout
    _set_default_template()


def update_default_layout(layout: go.Layout) -> None:
    """Update the default layout for plots.

    positional arguments:
      @ layout    : The layout object.
    """
    global default_layout
    set_default_layout(merge_layout(default_layout,
                                    layout,
                                    overwrite=False))


def set_default_renderer(renderer_name: str) -> None:
    """Change plotly's default renderer.

    positional_arguments:
      @ renderer_name : A plotly theme name like:
                         {"plotly_mimetype",
                          "browser",
                          "notebook[_connected]",
                          "iframe[_connected]"}
    """
    config = pio.renderers[pio.renderers.default.split('+')[0]].config
    pio.renderers.default = renderer_name
    set_default_config(config)
    pio.renderers._activate_pending_renderers()


def set_default_config(config: Dict[Any, Any]) -> None:
    """Change the default config for `go.Figure.show()`.
    List of the available configs is:
      https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js

    positional_arguments:
      @ config : Config keys and values.
    """
    pio.renderers[pio.renderers.default.split('+')[0]].config = config
