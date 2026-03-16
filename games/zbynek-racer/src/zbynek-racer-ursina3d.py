#!/usr/bin/env python3

from ursina import *

app = Ursina()
DirectionalLight()
AmbientLight(color=color.rgba(100,100,100,0.5))

def make_car():
    car = Entity()
    # Body
    Entity(parent=car, model='cube', color=color.azure, scale=(1, 0.3, 3))
    # Nose
    Entity(parent=car, model='cube', color=color.azure, scale=(0.4, 0.2, 1.2), position=(0, 0, 2))
    # Rear wing
    Entity(parent=car, model='cube', color=color.black, scale=(1.2, 0.1, 0.3), position=(0, 0.35, -1.4))
    # Front wing
    Entity(parent=car, model='cube', color=color.black, scale=(1.4, 0.1, 0.3), position=(0, 0.15, 3))

    wheel_width = 0.4
    wheel_mesh = Cylinder(radius=0.3, height=wheel_width, resolution=32)
    def make_wheel(x, z):
        #Entity(parent=car, model='cube', color=color.black, scale=(0.4, 0.4, 0.4), position=(x, 0, z))
        return Entity(
            parent=car,
            model=copy(wheel_mesh),
            color=color.black,
            position=(x - wheel_width/2, 0, z),
            rotation=(0,0,90),   # axle left-right
        )

    # Wheels
    car.wheels = []
    car.wheels.append(make_wheel(-0.9, 1.5))
    car.wheels.append(make_wheel(0.9, 1.5))
    car.wheels.append(make_wheel(-0.9, -1.5))
    car.wheels.append(make_wheel( 0.9, -1.5))

    return car

car = make_car()


# Camera
camera.position = (0, 3, -8)
car.rotation_y += 45
camera.look_at(car)

def update():
    car.rotation_y += 60 * time.dt
    for w in car.wheels:
        w.rotation_x += 600 * time.dt
        pass

app.run()
