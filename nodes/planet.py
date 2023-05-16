import glm
import moderngl as mgl
from moderngl_window.geometry import sphere

from base import Node
from loader import TextureLoader, ProgramLoader

class Planet(Node):
    def __init__(
        self,
        name,
        distance,
        solar_cycle,
        texture = "earth.jpg",
        is_retrograde = False
    ):
        super().__init__(
            program = ProgramLoader.load(vertex = "default", fragment = "planet"),
            vao = sphere(),
            texture = texture,
            mode = mgl.TRIANGLES
        )

        self.name = name
        self.distance = distance
        self.solar_cycle = solar_cycle
        self.velocity = (2 * glm.pi() * distance) / (solar_cycle * 100)
        self.direction = -1 if is_retrograde else 1

    def transform(self, time):
        self.translate([
            self.direction * self.distance * glm.sin(self.velocity * time),
            0,
            self.distance * glm.cos(self.velocity * time)
        ])

        self.rotate(time * 30, (0, 1, 0))
