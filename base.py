import glm

from loader import TextureLoader

class Camera:
    def __init__(self, projection):
        self.eye = (0, 0, 0)
        self.center = (0, 0, 0)
        self.up = (0, 1, 0)
        self.projection = projection

    def look_at(self, vector):
        self.center = vector

    def move_to(self, vector):
        self.eye = vector

    @property
    def view(self):
        return glm.lookAt(
            glm.vec3(*self.eye),
            glm.vec3(*self.center),
            glm.vec3(*self.up)
        )

class Scene:
    def __init__(self, nodes, aspect):
        self.camera = Camera(
            projection = glm.perspective(
                glm.radians(45),
                aspect,
                0.1,
                1000.0
            )
        )
        self.nodes = nodes

    def render(self, time):
        for node in self.nodes:
            node.program["view"].write(self.camera.view)
            node.program["projection"].write(self.camera.projection)
            node.render(time)

class Node:
    def __init__(self, program, texture, vao, mode):
        self.program = program
        self.texture = TextureLoader.load(texture) 
        self.vao = vao
        self.mode = mode
        self.model = glm.mat4(1.0)

    def translate(self, vector):
        self.model = glm.translate(self.model, vector)

    def rotate(self, angle, axis):
        self.model = glm.rotate(self.model, glm.radians(angle), axis)

    def scale(self, vector):
        self.model = glm.scale(self.model, vector)

    def transform(self, time):
        raise NotImplementedError

    def reset(self):
        self.model = glm.mat4(1.0)

    def render(self, time):
        self.texture.use()
        self.transform(time)
        self.program["model"].write(self.model)
        self.vao.render(self.program, self.mode)
        self.reset()
