from effects.particles import *
from meta.values import *

import math
import random
import colorsys


def shooting_lines_random(tick_delay, count=20, delay=2):
    for i in range(count):
        start_x = random.uniform(-17, 17)
        start_y = random.uniform(73, 87)
        start_z = random.uniform(55, 70)

        pitch = random.uniform(70, 89)
        yaw = random.uniform(0, 360)
        pr = math.radians(90 - pitch)
        yr = math.radians(yaw)

        dxz = math.cos(pr)
        dy = math.sin(pr)
        dx = dxz * math.sin(yr)
        dz = dxz * math.cos(yr)

        hue = random.random()
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

        particle_line(
            ticks_delay=tick_delay + i * delay,
            ticks_total=6,
            startpos=(start_x, start_y, start_z),
            endpos=(start_x + dx * 15, start_y + dy * 15, start_z + dz * 15),
            color=[r, g, b],
            scale=1.0,
            particles_per_tick=10,
        )


def lasers(tick_delay, count, delay):
    for i in range(0, count):
        random_point = random.choice(laser_points)
        endpos = (
            random_point[0] + random.uniform(-8, 8),
            random.uniform(86, 91),
            random_point[2] + random.uniform(-8, 8),
        )
        particle_line(
            ticks_delay=tick_delay + i * delay,
            ticks_total=6,
            startpos=random_point,
            endpos=endpos,
            color=random.choice(all_colors),
            scale=1.0,
            particles_per_tick=12,
        )
