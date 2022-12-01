#!/usr/bin/env python3

from .geometry.area import circle_area
from .geometry.polygon.area import triangle_area, rect_area


def main():
    print("circle area: %.3f" % circle_area(5))
    print("triangle area: %.3f" % triangle_area(5, 3))
    print("rectangle area: %.3f" % rect_area(5, 3))


if __name__ == '__main__':
    main()
