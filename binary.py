import matplotlib.pyplot as plt


def binary_graph(radicand: int, max_iterations: int):
    iterations_list = list()
    lp = 0
    rp = radicand

    for i in range(max_iterations):
        mid = (lp + rp) / 2
        iterations_list.append(mid)

        if mid**2 <= radicand:
            lp = mid
        else:
            rp = mid

    return iterations_list

def binary_method(radicand: int, max_iterations: int):
    lp = 0
    rp = radicand

    for counter in range(max_iterations):
        mid = (lp + rp) // 2

        if rp**2 == radicand:
            print(counter)
            break

        if mid**2 < radicand:
            lp = mid
        else:
            rp = mid

    return rp


if __name__ == '__main__':
    root = binary_method(radicand=999_999_961_946_176, max_iterations=51)
    print(root)

    iterations_list = binary_graph(radicand=225, max_iterations=25)
    plt.plot(iterations_list)
    plt.show()
