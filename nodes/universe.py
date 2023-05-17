import moderngl as mgl
from moderngl_window.geometry import cube, sphere

from base import Node
from loader import ProgramLoader

class Universe(Node):
    def __init__(self):
        super().__init__(
            program = ProgramLoader.load(vertex = "default", fragment = "universe"),
            vao = sphere(),
            texture = "universe.jpg",
            mode = mgl.TRIANGLES
        )

    def transform(self, time):
        self.scale([100, 100, 100])
        self.rotate(3 * time, (0, 1, 0))
