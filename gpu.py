import numpy as np
from numba import cuda
from base import GameOfLifeBase


@cuda.jit
def update_cell(before, after):
    x, y = cuda.grid(2)
    count = 0
    for i in (-1, 0, 1):
        if x + i < 0 or x + i >= before.shape[0]:
            continue
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue
            if y + j < 0 or y + j >= before.shape[1]:
                continue
            if before[x + i, y + j]:
                count += 1
    after[x, y] = count in (2, 3) if before[x, y] else count == 3


class GameOfLifeGPU(GameOfLifeBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device_state = (
            cuda.to_device(self.state),
            cuda.to_device(np.zeros(self.size, dtype=np.bool)),
        )

    def update(self):
        update_cell[self.size, 1](*self.device_state)
        self.state = self.device_state[1].copy_to_host()
        self.device_state = tuple(reversed(self.device_state))  # flip


if __name__ == '__main__':
    app = GameOfLifeGPU()
    app.start()
