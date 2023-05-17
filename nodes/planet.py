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
        texture,
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

class Planets:
    class Mercury(Planet):
        def __init__(self):
            super().__init__(
                name = "Mercúrio",
                texture = "mercury.png",
                distance = 2,
                solar_cycle = 0.24,
            )

    class Venus(Planet):
        def __init__(self):
            super().__init__(
                name = "Venus",
                texture = "venus.jpg",
                distance = 4,
                solar_cycle = 0.62,
                is_retrograde = True,
            )


    class Earth(Planet):
        def __init__(self):
            super().__init__(
                name = "Terra",
                texture = "earth.jpg",
                distance = 6,
                solar_cycle = 1,
            )

    class Mars(Planet):
        def __init__(self):
            super().__init__(
                name = "Marte",
                texture = "mars.jpg",
                distance = 8,
                solar_cycle = 1.88,
            )

    class Jupiter(Planet):
        def __init__(self):
            super().__init__(
                name = "Júpiter",
                texture = "jupiter.jpg",
                distance = 10,
                solar_cycle = 11.86,
            )

    class Saturn(Planet):
        def __init__(self):
            super().__init__(
                name = "Saturno",
                texture = "saturn.jpg",
                distance = 12,
                solar_cycle = 29.46,
            )

    class Uranus(Planet):
        def __init__(self):
            super().__init__(
                name = "Urano",
                texture = "uranus.jpg",
                distance = 14,
                solar_cycle = 84.01,
                is_retrograde = True,
            )

    class Neptune(Planet):
        def __init__(self):
            super().__init__(
                name = "Netuno",
                texture = "neptune.jpg",
                distance = 16,
                solar_cycle = 164.79,
            )
