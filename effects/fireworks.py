from meta.utils import *
import random
import colorsys


def rgb_to_decimal(color_rgb):
    """
    Accepts an [R, G, B] list in 0..255 range.
    Returns a normalized float tuple [r, g, b] in 0..1 range.
    """
    R = int(color_rgb[0] * 255)
    G = int(color_rgb[1] * 255)
    B = int(color_rgb[2] * 255)
    return (R << 16) + (G << 8) + B


def fireworks(ticks_delay, coords, color, shape, lifetime, flight_duration):
    """
    Summons a firework at each coordinate in coords using the provided color.
    color should be a decimal representing the Firework color (e.g. 2437522 for light blue).
    """
    for x, y, z in coords:
        cmd = f'summon firework_rocket {x} {y} {z} {{LifeTime:{lifetime},FireworksItem:{{id:firework_rocket,count:1,components:{{fireworks:{{flight_duration:{flight_duration},explosions:[{{shape:"{shape}",has_twinkle:false,has_trail:false,colors:[I;{rgb_to_decimal(color)}]}}]}}}}}}}}'

        scheduled_commands[ticks_delay].append(cmd)


def fireworks_random(ticks_delay, coords, lifetime=0, flight_duration=0, seed=393939):
    # Pick random shape
    shapes = ["burst", "small_ball", "large_ball", "star"]
    shape = random.choice(shapes)
    hue = random.random()
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    fireworks(ticks_delay, coords, [r, g, b], shape, lifetime, flight_duration)


def fireworks_burst(ticks_delay, coords, color, lifetime=0, flight_duration=0):
    fireworks(ticks_delay, coords, color, "burst", lifetime, flight_duration)


def fireworks_small_ball(ticks_delay, coords, color, lifetime=0, flight_duration=0):
    fireworks(ticks_delay, coords, color, "small_ball", lifetime, flight_duration)


def fireworks_large_ball(ticks_delay, coords, color, lifetime=0, flight_duration=0):
    fireworks(ticks_delay, coords, color, "large_ball", lifetime, flight_duration)


def fireworks_creeper(ticks_delay, coords, color, lifetime=0, flight_duration=0):
    fireworks(ticks_delay, coords, color, "creeper", lifetime, flight_duration)


def fireworks_star(ticks_delay, coords, color, lifetime=0, flight_duration=0):
    fireworks(ticks_delay, coords, color, "star", lifetime, flight_duration)
