import pyglet
from pyglet.gl import *
from pyglet.window import key, mouse

class MinecraftClone(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=800, height=600, caption="Minecraft Clone", resizable=True)
        self.set_exclusive_mouse(True)
        self.position = [0, 0, 0]
        self.rotation = [0, 0]
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.blocks = {}
        self.batch = pyglet.graphics.Batch()
        self.create_block(0, 0, 0)

    def create_block(self, x, y, z):
        """Add a block at the given position."""
        if (x, y, z) not in self.blocks:
            self.blocks[(x, y, z)] = self.batch.add(24, GL_QUADS, None,
                ('v3f', self.cube_vertices(x, y, z)),
                ('c3f', (0.5, 0.3, 0.2) * 24)
            )

    def remove_block(self, x, y, z):
        """Remove a block at the given position."""
        if (x, y, z) in self.blocks:
            self.blocks[(x, y, z)].delete()
            del self.blocks[(x, y, z)]

    def cube_vertices(self, x, y, z):
        """Return the vertices of a cube at position x, y, z."""
        return [
            x-0.5, y-0.5, z-0.5, x+0.5, y-0.5, z-0.5, x+0.5, y+0.5, z-0.5, x-0.5, y+0.5, z-0.5,  # Front
            x-0.5, y-0.5, z+0.5, x+0.5, y-0.5, z+0.5, x+0.5, y+0.5, z+0.5, x-0.5, y+0.5, z+0.5,  # Back
            x-0.5, y-0.5, z-0.5, x-0.5, y-0.5, z+0.5, x-0.5, y+0.5, z+0.5, x-0.5, y+0.5, z-0.5,  # Left
            x+0.5, y-0.5, z-0.5, x+0.5, y-0.5, z+0.5, x+0.5, y+0.5, z+0.5, x+0.5, y+0.5, z-0.5,  # Right
            x-0.5, y+0.5, z-0.5, x+0.5, y+0.5, z-0.5, x+0.5, y+0.5, z+0.5, x-0.5, y+0.5, z+0.5,  # Top
            x-0.5, y-0.5, z-0.5, x+0.5, y-0.5, z-0.5, x+0.5, y-0.5, z+0.5, x-0.5, y-0.5, z+0.5   # Bottom
        ]

    def on_draw(self):
        self.clear()
        glEnable(GL_DEPTH_TEST)
        glLoadIdentity()
        glRotatef(-self.rotation[0], 1, 0, 0)
        glRotatef(-self.rotation[1], 0, 1, 0)
        glTranslatef(-self.position[0], -self.position[1], -self.position[2])
        self.batch.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.rotation[0] += dy * 0.1
        self.rotation[1] += dx * 0.1

    def on_mouse_press(self, x, y, button, modifiers):
        x, y, z = map(int, self.position)
        if button == mouse.LEFT:
            self.remove_block(x, y, z)
        elif button == mouse.RIGHT:
            self.create_block(x, y, z)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.close()

    def update(self, dt):
        speed = dt * 10
        if self.keys[key.W]:
            self.position[2] -= speed
        if self.keys[key.S]:
            self.position[2] += speed
        if self.keys[key.A]:
            self.position[0] -= speed
        if self.keys[key.D]:
            self.position[0] += speed
        if self.keys[key.SPACE]:
            self.position[1] += speed
        if self.keys[key.LSHIFT]:
            self.position[1] -= speed

if __name__ == "__main__":
    window = MinecraftClone()
    pyglet.clock.schedule_interval(window.update, 1/60.0)
    pyglet.app.run()
