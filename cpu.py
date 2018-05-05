import numpy as np
from scipy import signal
from base import GameOfLifeBase


kernel = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])


class GameOfLifeCPU(GameOfLifeBase):

    def update(self):
        count = signal.convolve2d(self.state.astype(int), kernel, mode='same')
        self.state = self.state & (count == 2) | (count == 3)


if __name__ == '__main__':
    app = GameOfLifeCPU()
    app.start()
