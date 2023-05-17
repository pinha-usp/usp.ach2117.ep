#version 330

in vec2 uv;
in vec3 normal;
in vec3 fragPos;

uniform sampler2D tex;

void main() {
    vec3 lightColor = vec3(1.0);
    float ambientStrength = 0.2;
    vec3 ambient = ambientStrength * lightColor;

    vec3 lightPos = vec3(0.0);
    vec3 lightDir = normalize(lightPos - fragPos);
    vec3 norm = normalize(normal);

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    vec4 texColor = texture(tex, uv);

    gl_FragColor = texColor * vec4((ambient + diffuse), 1.0);
}
