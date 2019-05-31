def find_linear_equation(y0, x0, y1, y1):  # only first 2 points.
    m = (y0 - y1) / (x0 - x1)
    b = m * x0 - y0
    return 'y = {m}x + {b}'.format(m=m, b=b)  # you'll need to improve formatting.