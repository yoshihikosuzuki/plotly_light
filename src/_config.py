import plotly.io as pio


def set_theme(theme_name: str) -> None:
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
    """
    pio.templates.default = theme_name


def set_renderer(renderer_name: str) -> None:
    """Set plotly's default renderer.

    positional_arguments:
      @ renderer_name : A plotly theme name like:
                         {"plotly_mimetype",
                          "notebook[_connected]",
                          "browser",
                          "iframe[_connected]"}
    """
    pio.renderers.default = renderer_name
    # TODO: check if the following line is needed
    pio.renderers._activate_pending_renderers()
