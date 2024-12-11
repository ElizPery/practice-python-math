from math import pi, e


def simpson_integration(func, a, b, n):
    """
    Numerical integration by Simpson's method.

    :param func:The function that we integrate.
    :param a: Lower limit of integration.
    :param b: Upper limit of integration.
    :param n: Number of partitions.
    :return: The value of the integral.
    """
    h = (b - a) / n
    result = (func(a) + func(b))

    for i in range(1, n):
        if i%2 == 0:
            result += 2 * func(a + i * h)
        else:
            result += 4 * func(a + i * h)

    result *= h/3
    return result


def main_func(x):
  return 2*((4/(1.2*(2*pi)**0.5))*e**(-0.5*(((x-11)/1.2)**2)) + (7/(2.4*(2*pi)**0.5))*e**(-0.5*(((x-15)/2.4)**2)))


lower_limit = 9
upper_limit = 18
num_trapezoids = 10

integral_value = simpson_integration(main_func, lower_limit, upper_limit, num_trapezoids)
print(f"Integral value: {integral_value}")