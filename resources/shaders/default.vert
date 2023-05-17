#version 330

in vec3 in_position;
in vec3 in_normal;
in vec2 in_texcoord_0;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec2 uv; 
out vec3 normal;
out vec3 fragPos;

void main() {
    gl_Position = projection * view * model * vec4(in_position, 1.0);
    uv = in_texcoord_0;
    normal = mat3(transpose(inverse(model))) * in_normal;
    fragPos = vec3(model * vec4(in_position, 1.0));
}
