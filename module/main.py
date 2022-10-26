#!/usr/bin/env python3

# from geometry import circle_area
import geometry as gm


def main():
    print("circle area: %.3f" % gm.circle_area(5))
    print("triangle area: %.3f" % gm.triangle_area(5, 3))
    print("rectangle area: %.3f" % gm.rect_area(5, 3))


if __name__ == '__main__':
    main()
