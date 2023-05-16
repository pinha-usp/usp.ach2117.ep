import moderngl as mgl
from moderngl_window.geometry import sphere

from base import Node
from loader import ProgramLoader

class Sun(Node):
    def __init__(self):
        super().__init__(
            program = ProgramLoader.load(vertex = "default", fragment = "sun"),
            vao = sphere(),
            mode = mgl.TRIANGLES,
            texture = "sun.jpg"
        )

    def transform(self, time):
        self.scale([2, 2, 2])
        self.rotate(time * 20, (0, 1, 0))
