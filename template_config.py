"""
Template configuration extracted from OGtemplate.pptx
"""

from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

TEMPLATE_CONFIG = {
    'slide_width': 10.0,
    'slide_height': 5.625,
    'shapes': [
        # Text shapes
        {
            'name': 'Title',
            'left': 0.331,
            'top': 0.296,
            'width': 8.847,
            'height': 0.480,
            'font_size': 12.0,
            'text': 'YOUR TITLE HERE - Replace with your actual title',
        },
        {
            'name': 'AA1 Label',
            'left': 2.337,
            'top': 1.775,
            'width': 0.903,
            'height': 0.473,
            'font_size': 12.0,
            'text': 'AA1',
        },
        {
            'name': 'Notes',
            'left': 2.337,
            'top': 2.296,
            'width': 1.885,
            'height': 0.488,
            'font_size': 12.0,
            'text': 'FB Link\nIG Link',
        },
        {
            'name': 'Metrics',
            'left': 3.319,
            'top': 1.177,
            'width': 5.262,
            'height': 1.153,
            'font_size': 10.0,
            'text': 'Spend - $348.91 67.7%\nCAC (Hyros Scientific) - $58.15\nCAC (Hyros Last Click) - $43.61\nCAC (Clicks Only - Northbeam) - $57.58 (86.2%)\nCAC (Last non-direct touch - Northbeam) - $43.61 (∞%)\nNew Visits (Northbeam) - 51.23% (20.4%)\nECR (Northbeam) - 3.74% 603.2%\nDate Created - Jul 2, 2025',
        },
        # Image slots
        {
            'name': 'main_creative',
            'left': 0.33,
            'top': 1.22,
            'width': 2.01,
            'height': 3.47,
            'type': 'picture',
        },
        {
            'name': 'bottom_chart',
            'left': 4.86,
            'top': 3.18,
            'width': 5.00,
            'height': 1.71,
            'type': 'picture',
        },
        {
            'name': 'bottom_table',
            'left': 2.34,
            'top': 3.53,
            'width': 2.52,
            'height': 1.02,
            'type': 'picture',
        },
        {
            'name': 'logo',
            'left': 0.42,
            'top': 5.09,
            'width': 0.78,
            'height': 0.21,
            'type': 'picture',
        },
        {
            'name': 'mushroom_accent',
            'left': 7.47,
            'top': 1.05,
            'width': 3.43,
            'height': 1.64,
            'type': 'picture',
        },
        {
            'name': 'left_brush_stroke',
            'left': 0.51,
            'top': 0.94,
            'width': 2.01,
            'height': 0.15,
            'type': 'picture',
        },
        {
            'name': 'right_brush_stroke',
            'left': 8.70,
            'top': 0.54,
            'width': 1.19,
            'height': 1.71,
            'type': 'picture',
        },
    ]
}
