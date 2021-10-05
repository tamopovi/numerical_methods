import math


def f(x):
    return 3*math.sin(x)-1


def derivative(x):
    return 3*math.cos(x)


if __name__ == '__main__':
    print('Fixed point iteration')
    initial_approximation = float(input("Enter initial approximation: "))
    tolerance = float(input("Enter tolerance value: "))
    max_iterations_amount = int(input("Enter maximum iterations amount: "))

    # initial_approximation = 0
    # tolerance = 0.0001
    # max_iterations_amount = 100

    # p0:
    p = initial_approximation
    precision = 1
    iteration_count = 0

    result_array = []

    for i in range(max_iterations_amount):
        iteration_count = iteration_count+1
        p_next = f(p)
        precision = abs(p - p_next)
        result_array.append((i, p, precision))
        if(precision < tolerance):
            break
        else:
            p = p_next
    for i, val, _precision in result_array:
        print("i: %d, val: %f, |p - p0|: %f" % (i, val, _precision))

    print("Found in %d iterations" % (len(result_array)))

    print(abs(derivative(p)))
