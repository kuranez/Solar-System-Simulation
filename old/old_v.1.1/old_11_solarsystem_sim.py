"""
solarsystem_sim.py
Solar System Simulation v.1.1
@author: kuranez
https://github.com/kuranez/Solar-System-Simulation
"""

import constants
import pygame
import math
import itertools


# Solar system bodies
class Body:

    # Constants
    AU = 149.6e9  # Astronomical Unit, distance in meters
    G = 6.67428e-11  # Gravitational constant
    SCALE = 100 / AU  # 1 AU = 100 pixels
    TIMESTEP = 3600 * 24.0  # seconds in 1 day

    def __init__(self, x, y, radius, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass

        self.color = (0, 0, 0)

        self.sun = False
        self.distance_to_sun = 0

        self.orbit = []

        self.x_vel = 0.0
        self.y_vel = 0.0

        self.draw_line = True

    # Method to draw the bodies
    def draw(self, DISPLAYSURF):
        x = self.x * self.SCALE + constants.WIDTH / 2
        y = self.y * self.SCALE + constants.HEIGHT / 2

        if len(self.orbit) >= 3:  # min 3 points needed
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + constants.WIDTH / 2
                y = y * self.SCALE + constants.HEIGHT / 2
                updated_points.append((x, y))
            if self.draw_line:
                pygame.draw.lines(DISPLAYSURF, self.color, False,
                                  updated_points, 1)

        pygame.draw.circle(DISPLAYSURF, self.color, (x, y), self.radius)

    # Method to calculate force of attraction
    def attraction(self, other):
        # Coordinates
        other_x, other_y = other.x, other.y
        # Distances
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        # Total Distance
        distance = math.sqrt(distance_x**2 + distance_y**2)
        if other.sun:
            self.distance_to_sun = distance
        # Force
        force = self.G * self.mass * other.mass / distance**2
        # Angle
        theta = math.atan2(distance_y, distance_x)
        # Forces
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    # Method to update the position of the bodies
    def update_position(self, current_solarsystem):
        # Total forces, conservation of mass
        total_fx = total_fy = 0
        # Forces for each body in the solar system
        for body in current_solarsystem:
            if self == body:
                continue

            fx, fy = self.attraction(body)
            total_fx += fx
            total_fy += fy

        # Acceleration a = F / m
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # Update position with velocity
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


# Sun
class Sun(Body):

    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, radius, mass)
        self.sun = True
        self.color = constants.COLOR_SUN


# Planets
class Planet(Body):
    cycle_colors = itertools.cycle([
        constants.COLOR_MERCURY, constants.COLOR_VENUS, constants.COLOR_EARTH,
        constants.COLOR_MARS, constants.COLOR_JUPITER, constants.COLOR_SATURN,
        constants.COLOR_URANUS, constants.COLOR_NEPTUNE
    ])

    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, radius, mass)
        self.sun = False
        self.color = (next(Planet.cycle_colors))
