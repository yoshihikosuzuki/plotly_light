import plotly.io as pio

from ._const import colors

renderer = pio.renderers.default

# 300 dpi for 5-inch (13cm) plot = 1500 pixels
dpi = 300
plot_inch = 5

# Base is "simple_white", but the color and some appearances are changed.
theme = "simple_white"

# Base size of plots and font size. For font visibility, the font size is by default set as
# `font_size * (specified_plot_size / plot_size)` in the `layout` function.
plot_size = 500
font_size = 20
min_font_size = 16  # autoscaled font size will not be outside range of [min_fonrt_size, max_font_size]
max_font_size = 28
grid_width = 1
tick_len = 7
tick_width = 1.2
nticks_minor = 1
bounding_line_width = 1
zeroline_width = 1
legend_border_width = 1

margin = {"b": 10, "l": 10, "r": 10, "t": 50}

colorway = [
    colors["blue"],
    colors["yellow"],
    colors["red"],
    colors["darkblue"],
    colors["green"],
    colors["lightred"],
    colors["lightblue"],
    colors["darkred"],
    colors["lightgreen"],
    colors["purple"],
]

layout_axis = {
    "automargin": True,
    "title": {"standoff": 15},
    "ticks": "outside",
    "ticklen": tick_len,
    "tickwidth": tick_width,
    "tickcolor": "black",
    "showgrid": False,
    "gridcolor": "rgb(232,232,232)",
    "gridwidth": grid_width,
    "showline": True,
    "linecolor": "black",
    "linewidth": bounding_line_width,
    "zeroline": False,
    "zerolinecolor": "lightgray",
    "zerolinewidth": zeroline_width,
    "minor_nticks": nticks_minor + 1,
}

layout = {
    "width": plot_size,
    "height": plot_size,
    "annotationdefaults": {"arrowhead": 0, "arrowwidth": 1},
    "autotypenumbers": "strict",
    "coloraxis": {
        "colorbar": {"outlinewidth": 1, "tickcolor": "lightgray", "ticks": ""}
    },
    "colorscale": {
        "diverging": [
            [0.0, "rgb(103,0,31)"],
            [0.1, "rgb(178,24,43)"],
            [0.2, "rgb(214,96,77)"],
            [0.3, "rgb(244,165,130)"],
            [0.4, "rgb(253,219,199)"],
            [0.5, "rgb(247,247,247)"],
            [0.6, "rgb(209,229,240)"],
            [0.7, "rgb(146,197,222)"],
            [0.8, "rgb(67,147,195)"],
            [0.9, "rgb(33,102,172)"],
            [1.0, "rgb(5,48,97)"],
        ],
        "sequential": [
            [0.0, "#440154"],
            [0.1111111111111111, "#482878"],
            [0.2222222222222222, "#3e4989"],
            [0.3333333333333333, "#31688e"],
            [0.4444444444444444, "#26828e"],
            [0.5555555555555556, "#1f9e89"],
            [0.6666666666666666, "#35b779"],
            [0.7777777777777778, "#6ece58"],
            [0.8888888888888888, "#b5de2b"],
            [1.0, "#fde725"],
        ],
        "sequentialminus": [
            [0.0, "#440154"],
            [0.1111111111111111, "#482878"],
            [0.2222222222222222, "#3e4989"],
            [0.3333333333333333, "#31688e"],
            [0.4444444444444444, "#26828e"],
            [0.5555555555555556, "#1f9e89"],
            [0.6666666666666666, "#35b779"],
            [0.7777777777777778, "#6ece58"],
            [0.8888888888888888, "#b5de2b"],
            [1.0, "#fde725"],
        ],
    },
    "colorway": colorway,
    "paper_bgcolor": "white",
    "plot_bgcolor": "white",
    "font": {"color": "black", "family": "Arial", "size": font_size},
    "title": {"x": 0.05},
    "legend": {"bordercolor": "black", "borderwidth": legend_border_width},
    "shapedefaults": {"fillcolor": "black", "line": {"width": 0}, "opacity": 1},
    "margin": margin,
    "hovermode": "closest",
    "hoverlabel": {"align": "left"},
    "mapbox": {"style": "light"},
    "xaxis": layout_axis,
    "yaxis": layout_axis,
    "geo": {
        "bgcolor": "white",
        "lakecolor": "white",
        "landcolor": "white",
        "showlakes": True,
        "showland": True,
        "subunitcolor": "white",
    },
    "polar": {
        "angularaxis": {
            "gridcolor": "rgb(232,232,232)",
            "linecolor": "black",
            "showgrid": False,
            "showline": False,
            "ticks": "",
        },
        "bgcolor": "white",
        "radialaxis": {
            "gridcolor": "rgb(232,232,232)",
            "linecolor": "black",
            "showgrid": False,
            "showline": False,
            "ticks": "",
        },
    },
    "scene": {
        "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "rgb(232,232,232)",
            "gridwidth": 2,
            "linecolor": "black",
            "showbackground": True,
            "showgrid": False,
            "showline": False,
            "ticks": "",
            "zeroline": True,
            "zerolinecolor": "lightgray",
        },
        "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "rgb(232,232,232)",
            "gridwidth": 2,
            "linecolor": "black",
            "showbackground": True,
            "showgrid": False,
            "showline": False,
            "ticks": "",
            "zeroline": True,
            "zerolinecolor": "lightgray",
        },
        "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "rgb(232,232,232)",
            "gridwidth": 2,
            "linecolor": "black",
            "showbackground": True,
            "showgrid": False,
            "showline": False,
            "ticks": "",
            "zeroline": True,
            "zerolinecolor": "lightgray",
        },
    },
    "ternary": {
        "aaxis": {
            "gridcolor": "rgb(232,232,232)",
            "linecolor": "black",
            "showgrid": False,
            "showline": True,
            "ticks": "",
        },
        "baxis": {
            "gridcolor": "rgb(232,232,232)",
            "linecolor": "black",
            "showgrid": False,
            "showline": False,
            "ticks": "",
        },
        "bgcolor": "white",
        "caxis": {
            "gridcolor": "rgb(232,232,232)",
            "linecolor": "black",
            "showgrid": False,
            "showline": False,
            "ticks": "",
        },
    },
}

config = dict(
    showTips=False,
    displaylogo=False,
    modeBarButtonsToAdd=["hoverclosest", "hovercompare"],
    toImageButtonOptions=dict(format="svg"),
)
