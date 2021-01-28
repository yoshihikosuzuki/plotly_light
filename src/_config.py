from typing import Any, Optional, Dict
from dataclasses import dataclass
import plotly.io as pio
import plotly.graph_objects as go
from logzero import logger
from ._layout import make_layout


default_theme = pio.templates.default
default_layout = None


def _set_default_template_with_layout() -> None:
    """Set a custom template consisting of an existing theme and custom layout
    as the default template.
    """
    global default_theme, default_layout
    pio.templates["plotly_light"] = pio.templates.merge_templates(
        pio.templates[default_theme],
        go.layout.Template(layout=default_layout))
    pio.templates.default = "plotly_light"


def set_default_theme(theme_name: str,
                      use_default_layout: bool = True) -> None:
    """Set plotly's default theme.

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
      @ use_default_layout : If True, overwrite the theme's layout with the 
                             default layout set by `set_default_layout()`.
    """
    global default_theme
    pio.templates.default = default_theme = theme_name
    if use_default_layout and default_layout is not None:
        _set_default_template_with_layout()
    logger.info(f"Theme `{theme_name}` has been set.")


def set_default_layout(layout: go.Layout) -> None:
    """Set a default layout for plots.

    positional arguments:
      @ layout : The layout object.
    """
    global default_layout
    default_layout = layout
    _set_default_template_with_layout()


def set_default_renderer(renderer_name: str) -> None:
    """Set plotly's default renderer.

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
    logger.info(f"Renderer `{renderer_name}` has been set.")


def set_default_config(config: Dict[Any, Any]) -> None:
    """Set default config for `go.Figure.show()`. List of available configs is:

    https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js

    positional_arguments:
      @ config : Config keys and values.
    """
    pio.renderers[pio.renderers.default.split('+')[0]].config = config
