import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


class GameOfLifeBase:

    def __init__(self, state=None, size=(800, 600), interval=0):
        if state is None:
            state = np.random.randint(0, 2, size, dtype=np.bool)
        assert state.shape == size
        self.state = state
        self.size = size
        self.interval = interval  # ms
        self.image = None
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        self.frame = tk.Frame(master=self.root, width=size[0], height=size[1])
        self.frame.pack()
        self.canvas = tk.Canvas(self.frame, width=size[0], height=size[1], highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.root.after(0, self.step)

    def start(self):
        self.root.mainloop()

    def step(self):
        self.update()
        self.render()
        self.root.after(self.interval, self.step)

    def update(self):
        raise NotImplementedError()

    def render(self):
        image = Image.fromarray(np.uint8(self.state).T * 0xff)
        self.image = ImageTk.PhotoImage(image=image)
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.root.update()
