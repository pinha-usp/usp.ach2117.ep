from pathlib import Path

import moderngl as mgl
import moderngl_window as mglw

from base import Scene
from nodes.sun import Sun
from nodes.planet import Planets
from nodes.universe import Universe

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
                Universe(),
                Sun(),
                Planets.Mercury(),
                Planets.Venus(),
                Planets.Earth(),
                Planets.Mars(),
                Planets.Jupiter(),
                Planets.Saturn(),
                Planets.Uranus(),
                Planets.Neptune()
            ]
        )

        self.scene.camera.move_to((0, 20, -15))
        self.scene.camera.look_at((0, 0, 0))

    def render(self, time, frametime):
        self.ctx.clear()
        self.ctx.enable(mgl.DEPTH_TEST)
        self.ctx.enable(mgl.BLEND)

        self.texture.use()

        self.scene.render(time)
