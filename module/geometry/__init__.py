# This file is need to inform python to treat this directory as package

"""
If we don't import the files and functions here, we need to add the following in `main.py`:

from geometry.area import circle_area
from geometry.polygon.area import triangle_area, rect_area

Now that we are importing the functions here, we can rewrite our import in `main.py` as:

from geometry import circle_area, triangle_area, rect_area

or simply

import geometry

Also prefix the filename with . to tell python that `area.py` is in the current directory.
"""

from .area import circle_area
from .polygon.area import triangle_area, rect_area
