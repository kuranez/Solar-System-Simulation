"""
main.py
Solar System Simulation v.1.3
@author: kuranez
https://github.com/kuranez/Solar-System-Simulation
"""

import constants
import pygame
import sys
from pygame.locals import QUIT
from solarsystem_scale import scaled_sizes, calculate_scaled_sizes
from solarsystem_sim import Body, Sun, Planet

# Initialize pygame
pygame.init()

# Window Settings
DISPLAYSURF = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption('Solar System Simulation')

FONT_1 = pygame.font.SysFont(None, 21)

# Clock
clock = pygame.time.Clock()
FPS = 60
dt = 0

# Initialize the initial scale factor
initial_scale = 1.0  # Represents 100%
zoom_factor = initial_scale  # This will track the current zoom factor

# Solar System Creation

def create_solarsystem():
    """Create objects in the solar system using scaled sizes."""
    sun = Sun(0, 0, 2, constants.sun_mass)

    planets_data = [
        
        {"name": "Mercury", 
         "position": -0.387 * Planet.AU, 
         "scaled_size": scaled_sizes["Mercury"], 
         "mass": constants.mercury_mass, 
         "is_inner": True, 
         "velocity": constants.mercury_velocity},
        
        {"name": "Venus", 
         "position": -0.723 * Planet.AU, 
         "scaled_size": scaled_sizes["Venus"], 
         "mass": constants.venus_mass, 
         "is_inner": True, 
         "velocity": constants.venus_velocity},
        
        {"name": "Earth", 
         "position": -1 * Planet.AU, 
         "scaled_size": scaled_sizes["Earth"], 
         "mass": constants.earth_mass, "is_inner": True, 
         "velocity": constants.earth_velocity},
        
        {"name": "Mars", 
         "position": -1.524 * Planet.AU, 
         "scaled_size": scaled_sizes["Mars"], 
         "mass": constants.mars_mass, 
         "is_inner": True, 
         "velocity": constants.mars_velocity},
        
        {"name": "Jupiter", 
         "position": -5.204 * Planet.AU, 
         "scaled_size": scaled_sizes["Jupiter"], 
         "mass": constants.jupiter_mass, 
         "is_inner": False, 
         "velocity": constants.jupiter_velocity},
        
        {"name": "Saturn", 
         "position": -9.573 * Planet.AU, 
         "scaled_size": scaled_sizes["Saturn"], 
         "mass": constants.saturn_mass, 
         "is_inner": False, 
         "velocity": constants.saturn_velocity},
        
        {"name": "Uranus", 
         "position": -19.165 * Planet.AU, 
         "scaled_size": scaled_sizes["Uranus"], 
         "mass": constants.uranus_mass, 
         "is_inner": False, 
         "velocity": constants.uranus_velocity},
        
        {"name": "Neptune", 
         "position": -30.178 * Planet.AU, 
         "scaled_size": scaled_sizes["Neptune"], 
         "mass": constants.neptune_mass, "is_inner": False, 
         "velocity": constants.neptune_velocity},
    ]

    planets = []
    for data in planets_data:
        planet = Planet(data["position"], 
                        0, 
                        data["scaled_size"], 
                        data["mass"], 
                        name=data["name"],
                        is_inner_planet=data["is_inner"])
        planet.y_vel = data["velocity"]
        planet.draw_line = True
        planets.append(planet)

    # Toggle orbit line for the Sun
    sun.draw_line = False  
    
    return [sun] + planets

# Create solar system 
solarsystem = create_solarsystem()

# Assign individual planet variables
sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune = solarsystem

# # Inner and Outer Planets
# inner_planets = [mercury, venus, earth, mars]  
# outer_planets = [jupiter, saturn, uranus, neptune]

# Current Solar System
current_solarsystem = solarsystem

# Render Menu Text

def render_menu_texts():
    # Displaying FPS in the upper left corner
    fps_text = "FPS: " + str(int(clock.get_fps()))
    
    # Render FPS in the upper left corner
    fps_surface = FONT_1.render(fps_text, True, constants.COLOR_TEXT)
    DISPLAYSURF.blit(fps_surface, (15, 15))

    # Displaying title in the upper right corner
    title = "Solar System Simulation v.1.3"
    title_surface = FONT_1.render(title, True, constants.COLOR_TEXT)

    # Calculate position for upper right corner
    title_width, title_height = title_surface.get_size()
    upper_right_x = DISPLAYSURF.get_width() - title_width - 15
    upper_right_y = 15
    
    DISPLAYSURF.blit(title_surface, (upper_right_x, upper_right_y))

    # Displaying navigation texts in the lower right corner
    navigation_texts = [
        "Navigation:",
        "Press UP / DOWN to adjust Simulation Scale",
        "Press RIGHT / LEFT to adjust Simulation Speed",
        # "Press Q or Number Keys 1-8 to toggle Orbit Lines",
        # "Press A to show all Planets",
        # "Press S to show Inner Planets",
        # "Press D to show Outer Planets"
    ]

    # Prepare surfaces for navigation texts
    navigation_surfaces = [FONT_1.render(text, True, constants.COLOR_TEXT) for text in navigation_texts]
    
    # Initial position for lower right corner navigation
    lower_right_x = DISPLAYSURF.get_width() - 15  # Right aligned
    lower_right_y = DISPLAYSURF.get_height() - 100  # Fixed starting y position

    # Render each navigation item with 15px spacing
    for i, surface in enumerate(navigation_surfaces):
        surface_width, surface_height = surface.get_size()
        DISPLAYSURF.blit(surface, (lower_right_x - surface_width, lower_right_y + i * (surface_height + 15)))  # 15 pixels spacing

    # Displaying planet distance texts in the lower left corner
    distance_title = "Distance from the Sun:"
    planet_distances = [
        ("Mercury", mercury, constants.COLOR_MERCURY),
        ("Venus", venus, constants.COLOR_VENUS),
        ("Earth", earth, constants.COLOR_EARTH),
        ("Mars", mars, constants.COLOR_MARS),
        ("Jupiter", jupiter, constants.COLOR_JUPITER),
        ("Saturn", saturn, constants.COLOR_SATURN),
        ("Uranus", uranus, constants.COLOR_URANUS),
        ("Neptune", neptune, constants.COLOR_NEPTUNE)
    ]

    distance_title_surface = FONT_1.render(distance_title, True, constants.COLOR_TEXT)
    DISPLAYSURF.blit(distance_title_surface, (15, 475))

    # Adjusting spacing for planet distances (5 pixels narrower)
    for i, (name, planet, color) in enumerate(planet_distances):
        distance_text = f"{name}: {round(planet.distance_to_sun / 1000, 1)} km"
        surface = FONT_1.render(distance_text, True, color)
        DISPLAYSURF.blit(surface, (15, 505 + i * 25))  # 25 pixels between each item


# Main Loop
while True:
    clock.tick(FPS)
    DISPLAYSURF.fill(constants.COLOR_BACKGROUND)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Adjust Simulation Scale
            if event.key == pygame.K_UP:
                zoom_factor *= 1.1 # Increase zoom factor by 10%
                Body.SCALE += 10 / Body.AU
            elif event.key == pygame.K_DOWN:
                zoom_factor *= 0.9 # Decrease zoom factor by 10%
                Body.SCALE -= 10 / Body.AU
    
            # Recalculate planet sizes based on the updated zoom factor
            scaled_sizes = calculate_scaled_sizes(zoom_factor)

            # Adjust Simulation Speed
            if event.key == pygame.K_RIGHT:
                Body.TIMESTEP += 3600 * 24
            elif event.key == pygame.K_LEFT:
                Body.TIMESTEP -= 3600 * 24

            # # Toggle Orbit Lines on/off
            # if event.key == pygame.K_q:
            #     for planet in solarsystem[1:]:
            #         planet.draw_line = not planet.draw_line
            # elif event.key == pygame.K_1:
            #     mercury.draw_line = not mercury.draw_line
            # elif event.key == pygame.K_2:
            #     venus.draw_line = not venus.draw_line
            # elif event.key == pygame.K_3:
            #     earth.draw_line = not earth.draw_line
            # elif event.key == pygame.K_4:
            #     mars.draw_line = not mars.draw_line
            # elif event.key == pygame.K_5:
            #     jupiter.draw_line = not jupiter.draw_line
            # elif event.key == pygame.K_6:
            #     saturn.draw_line = not saturn.draw_line
            # elif event.key == pygame.K_7:
            #     uranus.draw_line = not uranus.draw_line
            # elif event.key == pygame.K_8:
            #     neptune.draw_line = not neptune.draw_line

            # # Toggle Planets on/off
            # if event.key == pygame.K_a:
            #     current_solarsystem = solarsystem
            # elif event.key == pygame.K_s:
            #     current_solarsystem = inner_planets
            # elif event.key == pygame.K_d:
            #     current_solarsystem = outer_planets

    # Draw and update Solar System, new sizes
    for body in current_solarsystem:
        if isinstance(body, Planet):  # Only apply scaling and toggling to planets
            body.radius = scaled_sizes[body.name] # Update radius based on zoom factor
            body.update_position(current_solarsystem) # Update positions of bodies
            body.draw(DISPLAYSURF)
        else:
            body.draw(DISPLAYSURF)  # Just draw the Sun as is, with no scaling or orbit lines

    # Render menu texts and planet distances
    render_menu_texts()

    # delta time for framerate-independent physics
    dt = clock.tick(FPS) / 1000
    

    # Update display
    pygame.display.update()
    