import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 3*math.sin(x)-1 - x


def is_pos(x):
    return x > 0


def validate_input_for_bisection_method(a, b):
    return (is_pos(f(a)) and not(is_pos(f(b)))) or (is_pos(f(b)) and not(is_pos(f(a))))


GRAPH_ACCURACY = 0.1


def create_function_points(func, start, end):
    points = []
    for number in np.arange(start, end, GRAPH_ACCURACY):
        points.append(func(number))
    return points


def draw_graph(start, end, res, func):
    points = create_function_points(func, start, end)
    plt.axhline(y=0, color='r', linestyle=':')
    print([x[2] for x in res])

    x = [x[2] for x in res]
    y = [f(x[2]) for x in res]
    indexes = np.arange(len(res))
    plt.plot(np.arange(start, end, GRAPH_ACCURACY), points)
    for index in indexes:
        plt.scatter(x, y, marker='x', color='red')
        plt.text(x[index], y[index], index, fontsize=9)
    plt.grid(True)
    plt.show()


error_val = 0.0000001

if __name__ == '__main__':
    cycles = 100
    result_array = []
    while True:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        res = validate_input_for_bisection_method(a, b)
        if(res == False):
            print("a, b input values must pass validation for bisection method")
        if(res == True):
            print("a, f(%f): %f" % (a, f(a)))
            print("b, f(%f): %f" % (b, f(b)))
            break

    while(cycles > 0 and abs(a-b) > error_val):
        c = (a+b) / 2
        x = f(a) / f(b)
        cycles = cycles - 1
        if (x == 0):
            break
        else:
            result_array.append((a, b, c))
            if(validate_input_for_bisection_method(c, b)):
                a = c
                # print("[%f,%f]" % (a, b))
            elif(validate_input_for_bisection_method(a, c)):
                b = c
                # print("[%f,%f]" % (a, b))

    print("Calcualted in: %d cycles" % (100-cycles))

    for i, iteration in (enumerate(result_array)):
        print("i: %d, a: %f, b: %f, c: %f" %
              (i, iteration[0], iteration[1], iteration[2]))
    min = result_array[0][0]
    max = result_array[0][1]

    draw_graph(min, max, result_array, f)
