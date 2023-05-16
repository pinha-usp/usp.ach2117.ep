from pathlib import Path
from moderngl import Program
from moderngl_window import resources
from moderngl_window.meta import ProgramDescription, TextureDescription

resources.register_texture_dir(
    Path("resources/textures").absolute()
)

resources.register_program_dir(
    Path("resources/shaders").absolute()
)

class TextureLoader:

    @classmethod
    def load(
        cls,
        name: str
    ):
        desc = TextureDescription(
            path = name
        )

        return resources.textures.load(desc)

class ProgramLoader:

    loaded = {}

    @classmethod
    def load(
        cls,
        both: str = None,
        vertex: str = None,
        fragment: str = None
    ) -> Program:
        vert, frag = (vertex, fragment) if both is None else (both, both)

        if not vert or not frag:
            raise ValueError("Choose either both or vertex and fragment")

        desc = ProgramDescription(
            vertex_shader = f"{vert}.vert",
            fragment_shader = f"{frag}.frag",
        )

        key = (vert, frag)

        if key not in cls.loaded:
            cls.loaded[key] = resources.programs.load(desc)

        return cls.loaded[key]
