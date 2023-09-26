import numpy as np


def lattice_paths(grid):
    lattice = np.zeros((grid + 1) ** 2).reshape((grid + 1), -1)
    lattice[0] = 1
    lattice[range(0, (grid + 1)), 0] = 1
    idx = 0
    print(lattice)
    for i in lattice:
        for index, value in enumerate(i):
            if value == 0:
                lattice[idx, index] = lattice[idx - 1, index] + lattice[idx, index - 1]
        idx += 1
    return int(lattice[grid, grid])


print(lattice_paths(20))
