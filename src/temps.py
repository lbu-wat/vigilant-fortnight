#!/usr/bin/env python3

from tabulate import tabulate


def f2c(f):
    return round((f - 32) * 5 / 9, 2)


if __name__ == '__main__':
    temps = [[f, f2c(f)] for f in range (30, 60)]

    print(tabulate(temps, headers=['F', 'C'], tablefmt='fancy_grid'))
