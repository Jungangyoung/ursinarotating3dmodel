

from ursina import *

app = Ursina()

# Load the 3D character model
character = Entity(
    model='sample.glb',
    position=(0, 0, 0),
    scale=3
)

# Settings
move_speed = 4
rotation_speed = 50
turn_speed = 100

def update():
    # Continuous automatic rotation
    character.rotation_y += rotation_speed * time.dt

    # Movement: W/S forward and backward
    character.position += character.forward * (
        held_keys['w'] - held_keys['s']
    ) * move_speed * time.dt

    # Movement: A/D left and right
    character.position += character.right * (
        held_keys['d'] - held_keys['a']
    ) * move_speed * time.dt

    # Manual rotation: Q/E
    character.rotation_y += (
        held_keys['e'] - held_keys['q']
    ) * turn_speed * time.dt

    # Move up and down
    character.y += (
        held_keys['space'] - held_keys['left shift']
    ) * move_speed * time.dt

# Camera
camera.position = (0, 3, -8)
camera.look_at(character)

# Lighting
DirectionalLight().look_at(Vec3(1, -1, -1))
AmbientLight(color=color.rgba(100, 100, 100, 255))

# Start game
app.run()
