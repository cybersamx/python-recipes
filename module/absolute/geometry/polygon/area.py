from geometry.multiply import multiply
from fmt.log import println


def triangle_area(h, b):
    println("triangle_area called")
    return 0.5 * multiply(h, b)


def rect_area(l, w):
    println("rect_area called")
    return multiply(l, w)
