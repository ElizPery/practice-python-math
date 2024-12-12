from math import pi, exp, sqrt

def rectangle_integration(func, a, b, n):
    """
    Numerical integration by rectangle method.

    :param func:The function that we integrate.
    :param a: Lower limit of integration.
    :param b: Upper limit of integration.
    :param n: Number of rectangles (split).
    :return: The value of the integral.
    """
    h = (b - a) / n
    result = 0

    for i in range(1, n+1):
        result += func(a + i * h - h/2)

    result *= h
    return result

def trapezoidal_integration(func, a, b, n):
    """
    Numerical integration by trapezoid method.

    :param func:The function that we integrate.
    :param a: Lower limit of integration.
    :param b: Upper limit of integration.
    :param n: Number of trapezoids (partitions).
    :return: The value of the integral.
    """
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        result += func(a + i * h)

    result *= h
    return result

main_func = lambda x: 2*((4/(1.2*sqrt(2*pi)))*exp(-0.5*(((x-11)/1.2)**2)) + (7/(2.4*sqrt(2*pi)))*exp(-0.5*(((x-15)/2.4)**2)))

lower_limit = 9
upper_limit = 18
num_trapezoids = 10

integral_value = rectangle_integration(main_func, lower_limit, upper_limit, num_trapezoids)
print(f"Integral value: {integral_value}")

integral_value2 = trapezoidal_integration(main_func, lower_limit, upper_limit, num_trapezoids)
print(f"Integral value: {integral_value2}")