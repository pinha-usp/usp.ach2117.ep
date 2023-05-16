from pathlib import Path

import moderngl as mgl
import moderngl_window as mglw

from base import Scene
from nodes.sun import Sun
from nodes.planet import Planet

class Window(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "Simulação do Sistema Solar"
    resource_dir = Path("resources")
    fullscreen = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.texture = self.load_texture_2d("textures/sun.jpg")

        self.scene = Scene(
            aspect = self.aspect_ratio,
            nodes = [
                Sun(),
                Planet(
                    name = "Mercúrio",
                    texture = "mercury.png",
                    distance = 2,
                    solar_cycle = 0.24
                ),
                Planet(
                    name = "Venus",
                    texture = "venus.jpg",
                    distance = 4,
                    solar_cycle = 0.62,
                    is_retrograde = True
                ),
                Planet(
                    name = "Terra",
                    texture = "earth.jpg",
                    distance = 6,
                    solar_cycle = 1
                ),
                Planet(
                    name = "Marte",
                    texture = "mars.jpg",
                    distance = 8,
                    solar_cycle = 1.88
                ),
                Planet(
                    name = "Júpiter",
                    texture = "jupiter.jpg",
                    distance = 10,
                    solar_cycle = 11.86
                ),
                Planet(
                    name = "Saturno",
                    texture = "saturn.jpg",
                    distance = 12,
                    solar_cycle = 29.46
                ),
                Planet(
                    name = "Urano",
                    texture = "uranus.jpg",
                    distance = 14,
                    solar_cycle = 84.01,
                    is_retrograde = True
                ),
                Planet(
                    name = "Netuno",
                    texture = "neptune.jpg",
                    distance = 16,
                    solar_cycle = 164.79
                ),
            ]
        )

        self.scene.camera.move_to((0, 5, 22))
        self.scene.camera.look_at((0, -5, 0))

    def render(self, time, frametime):
        self.ctx.clear()
        self.ctx.enable(mgl.DEPTH_TEST)

        self.texture.use()

        self.scene.render(time)
