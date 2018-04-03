"""

Tests sur les lambdas python 3

"""


def lambda_simple():
    """
    Simple lambda example with map

    map(function_to_apply, list_of_inputs)

    :return:
    """
    items = [1, 2, 3, 4, 5]
    squared = []
    for i in items:
        squared.append(i ** 2)

    squared2 = list(map(lambda x: x ** 2, items))

    print(squared == squared2)


def star(f):
    """
    For Return a lambda function that takes arguments with a *
    The * is just Pythons way of telling a function
    "please use the elements of whatever follows as your arguments and not the thing itself!"

    :param f:
    :return:
    """
    return lambda args: f(*args)


def lambda_multiple_variable():
    """
    Multiple variable lambda
    """
    # When you want to parse two elements in a lambda
    points = [(1, 2), (2, 3)]
    result = list(map(lambda p: p[0] * p[0] + p[1] * p[1], points))
    print(result)

    result = list(map(star(lambda x, y: (x * x + y * y)), points))
    print(result)


def lambda_2to3():
    """
    As tuple parameters are used by lambdas because of the single expression limitation, they must also be supported. This is done by having the expected sequence argument bound to a single parameter and then indexing on that parameter:

    lambda (x, y): x + y

    will be translated into:

    lambda x_y: x_y[0] + x_y[1]
    :return:
    """
    pass


def lambda_indexing():
    """
    lambda with indexing, value multiplied by its index
    """
    a = [1, 3, 5, 6, 8]
    am = map(lambda i_el: i_el[0] * i_el[1], enumerate(a))
    print(list(am))


def lambda_dictionary():
    """
    Lambda in dictionary
    """
    t = {'A': 2, 'B': 1}
    ts = sorted(t.items(), key=lambda k_v: k_v[1], )
    print(ts)


def zip_instead():
    """
    zip takes (in the simplest case) two lists and "zips" them: zip([1,2,3], [4,5,6]) will become [(1,4), (2,5), (3,6)].
    So if you consider the outer list to be a matrix and the inner tuples to be the rows,
    that's a transposition (ie., we turned the rows to columns).
    """
    # Using zip instead of lambda
    result = zip([1, 2, 3], [4, 5, 6])
    print(list(result))
    # The equivalent
    lis = [[1, 2, 3], [4, 5, 6]]
    result = zip(*lis)
    print(list(result))


def zip_demo():
    """
    Howw zip works

    :return:
    """
    coordinate = ['x', 'y', 'z']
    value = [3, 4, 5, 0, 9]

    result = zip(coordinate, value)
    result_list = list(result)
    print(result_list)

    c, v = zip(*result_list)
    print('c =', c)
    print('v =', v)


if __name__ == "__main__":
    lambda_simple()
    lambda_dictionary()
    lambda_indexing()
    lambda_multiple_variable()
    zip_instead()
    zip_demo()