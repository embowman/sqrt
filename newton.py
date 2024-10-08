import matplotlib.pyplot as plt


def newton_graph(radicand: int, max_iterations: int):
    return list((i + radicand / i) / 2 for i in range(1, max_iterations))

def newton_method(radicand: int, max_iterations: int):
    prev = radicand

    for counter in range(max_iterations):
        curr = (prev + radicand / prev) / 2

        if curr >= prev:
            print(counter)
            break

        prev = curr

    return round(prev)


if __name__ == '__main__':
    root = newton_method(radicand=999_999_961_946_176, max_iterations=31)
    print(root)

    iterations_list = newton_graph(radicand=225, max_iterations=25)
    plt.plot(iterations_list)
    plt.show()
