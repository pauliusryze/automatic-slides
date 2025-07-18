"""
Template configuration extracted from template.pptx
"""

from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

TEMPLATE_CONFIG = {
    'slide_width': 13.330,
    'slide_height': 7.500,
    'shapes': [
        {
            'name': 'Title',
            'left': 0.500,
            'top': 0.200,
            'width': 12.054,
            'height': 0.640,
            'font_size': 12.0,
            'text': '''MED - REELS - INHOUSE - MC 2025 05 29 - Cortisol Belly - If you have alcohol belly, just stop drinking alcohol. - AIRIDAS/NENAD - CHARLES - Rron''',
        },
        {
            'name': 'Main Image',
            'left': 0.733,
            'top': 1.113,
            'width': 3.486,
            'height': 3.874,
            'font_size': 0.0,
            'type': 'picture',
        },
        {
            'name': 'Metrics',
            'left': 6.360,
            'top': 1.603,
            'width': 6.327,
            'height': 2.255,
            'font_size': 16.0,
            'text': '''Spend - $348.91 67.7%
CAC (Hyros Scientific) - $58.15
CAC (Hyros Last Click) - $43.61
CAC (Clicks Only - Northbeam) - $57.58 (86.2%)
CAC (Last non-direct touch - Northbeam) - $43.61 (∞%)
New Visits (Northbeam) - 51.23% (20.4%)
ECR (Northbeam) - 3.74% 603.2%
Date Created - Jul 2, 2025''',
        },
        {
            'name': 'Notes',
            'left': 4.356,
            'top': 3.921,
            'width': 5.500,
            'height': 0.500,
            'font_size': 10.0,
            'text': '''FB Link | IG Link''',
        },
        {
            'name': 'Bottom Image 1',
            'left': 0.500,
            'top': 5.300,
            'width': 4.500,
            'height': 1.500,
            'font_size': 0.0,
            'type': 'picture',
        },
        {
            'name': 'Bottom Image 2',
            'left': 5.200,
            'top': 4.486,
            'width': 7.800,
            'height': 2.461,
            'font_size': 0.0,
            'type': 'picture',
        },
        {
            'name': 'AA1 Label',
            'left': 4.356,
            'top': 2.548,
            'width': 1.287,
            'height': 0.640,
            'font_size': 32.0,
            'text': '''AA1''',
        },
    ]
}
