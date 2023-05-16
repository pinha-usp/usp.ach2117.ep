#version 330

in vec3 in_position;
in vec3 in_normal;
in vec2 in_texcoord_0;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec2 uv; 

void main() {
    gl_Position = projection * view * model * vec4(in_position, 1.0);
    uv = in_texcoord_0;
}
