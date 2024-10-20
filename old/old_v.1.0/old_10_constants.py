"""
constants.py
Solar System Simulation v.1.0
@author: kuranez
https://github.com/kuranez/Solar-System-Simulation
"""

import pygame

# Display Variables
WIDTH, HEIGHT = 935, 725

COLOR_TEXT = (255, 255, 255)
COLOR_BACKGROUND = (36, 36, 36)

# Solar System Colors
COLOR_SUN = (252, 150, 1)
COLOR_MERCURY = (173, 168, 165)
COLOR_VENUS = (227, 158, 28)
COLOR_EARTH = (107, 147, 214)
COLOR_MARS = (193, 68, 14)
COLOR_JUPITER = (216, 202, 157)
COLOR_SATURN = (191, 189, 175)
COLOR_URANUS = (209, 231, 231)
COLOR_NEPTUNE = (63, 84, 186)

# Astronomical Unit, distance in meters
AU = 149.6e9
# Gravitational constant
G = 6.67428e-11
# 1 AU = 400 pixels
SCALE = 400 / AU
# seconds in 1 day
TIMESTEP = 3600 * 24

# Sun Data
sun_radius = 1392700e3 / 2
sun_mass = 1.98892e30

# Planetary Data
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/

# Perihelion in meters
mercury_perihelion = 46.0e9
venus_perihelion = 107.5e9
earth_perihelion = 147.1e9
mars_perihelion = 206.7e9
jupiter_perihelion = 740.6e9
saturn_perihelion = 1357.6e9
uranus_perihelion = 2732.7e9
neptune_perihelion = 4471.1e9

# Radius in meters
mercury_radius = 4879e3 / 2
venus_radius = 12104e3 / 2
earth_radius = 12756e3 / 2
mars_radius = 6792e3 / 2
jupiter_radius = 142984e3 / 2
saturn_radius = 120536e3 / 2
uranus_radius = 51118e3 / 2
neptune_radius = 49528e3 / 2

# Mass in kilograms
mercury_mass = 0.330e24
venus_mass = 4.870e24
earth_mass = 5.970e24
mars_mass = 0.642e24
jupiter_mass = 1898e24
saturn_mass = 568e24
uranus_mass = 86.800e24
neptune_mass = 102e24

# Orbital velocity in meters per second
mercury_velocity = 47.40e3
venus_velocity = 35.02e3
earth_velocity = 29.78e3
mars_velocity = 24.06e3
jupiter_velocity = 13.06e3
saturn_velocity = 9.68e3
uranus_velocity = 6.80e3
neptune_velocity = 5.43e3
