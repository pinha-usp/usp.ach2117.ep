#version 330

in vec2 uv;
uniform sampler2D tex;

void main() {
    vec4 texColor = texture(tex, uv);
    texColor.a *= 0.2;
    gl_FragColor = texColor; 
}
