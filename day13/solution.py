from functools import reduce

import math

from read_file.read_file import read_file


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


if __name__ == '__main__':
    lines = read_file("input.txt")

    earliest_departure = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]


    def minutes_to_wait(bus):
        next_departure = math.ceil(earliest_departure / bus) * bus
        return next_departure - earliest_departure


    best_bus, lowest_minutes_to_wait = min(((bus, minutes_to_wait(bus)) for bus in buses), key=lambda a: a[1])
    answer_part_1 = best_bus * lowest_minutes_to_wait
    print(f"Part 1: {answer_part_1}")

    delays = [-delay for delay, bus in enumerate(lines[1].split(",")) if bus != "x"]

    earliest_time = chinese_remainder(buses, delays)
    print(f"Part 2: {earliest_time}")
