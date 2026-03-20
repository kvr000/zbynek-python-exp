#!/usr/bin/env python3
import math

from ursina import Ursina, DirectionalLight, AmbientLight, Entity, Cylinder, color, copy, camera, time, Mesh, Vec3, \
    application


class Meshes:
    @staticmethod
    def prism(base: list[tuple[float]], peak: tuple[float], add_base=False) -> Mesh:
        """
        Generates side triangles of an open prism.
        base: list of (x,y,z) tuples for base vertices
        peak: (x,y,z) tuple for the top vertex
        The base is NOT closed; you can handle base closure externally.
        """
        vertices = [Vec3(*v) for v in base]
        peak_vertex = Vec3(*peak)
        vertices.append(peak_vertex)
        peak_index = len(vertices) - 1

        triangles = []
        n = len(base)

        # Connect consecutive base vertices to the peak
        # Only i from 0..n-2, last edge is handled externally
        for i in range(n-1):
            triangles.append((i, i+1, peak_index))
        if add_base:
            for i in range(len(base) - 2):
                triangles.append((0, i + 2, i + 1))

        return Mesh(vertices=vertices, triangles=triangles, mode='triangle')


app = Ursina()
DirectionalLight()
AmbientLight(color=color.rgba(100,100,100,0.5))

stopped = False


class ShowItem(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_model()
        self.rotation_y += 45

    def load_model(self):
        # Body
        Entity(parent=self, model='ShowItem', color=color.azure, scale=1)

    def update(self):
        if not stopped:
            self.rotation_y += 60 * time.dt


car = ShowItem()

def input(key):
    global stopped
    if key == 'space':
        stopped = not stopped
    elif key == 'escape':
        application.quit()

# Camera
camera.position = (0, 3, -8)
camera.look_at(car)

app.run()
