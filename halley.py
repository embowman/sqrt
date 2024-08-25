import matplotlib.pyplot as plt


def halley_graph(radicand: int, max_iterations: int):
    numerators_list = list()
    denominators_list = list()

    for i in range(max_iterations):
        numerators_list.append(i**2 + 3 * radicand)
        denominators_list.append(i**2 * 3 + radicand)

    return numerators_list, denominators_list

def halley_method(radicand: int, max_iterations: int):
    prev = 1

    for counter in range(max_iterations):
        numerator = prev**2 + 3 * radicand
        denominator = prev**2 * 3 + radicand
        curr = prev * (numerator / denominator)

        if numerator <= denominator:
            print(counter)
            break

        prev = curr

    return prev


if __name__ == '__main__':
    root = halley_method(radicand=999_999_961_946_176, max_iterations=20)
    print(round(root))

    numerators_list, denominators_list = halley_graph(radicand=225, max_iterations=25)
    plt.plot(numerators_list)
    plt.plot(denominators_list)
    plt.show()
