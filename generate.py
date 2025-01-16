#!/usr/bin/env python3

from effects.particles import *

from parts.stands import *
from parts.lines import *
from parts.fireworks import *
from meta.values import *

from meta.utils import *

random.seed(393939)


def shape_sequence():
    particle_line(
        ticks_delay=0,
        ticks_total=6,
        startpos=(3, 71, 58),
        endpos=(11, 89, 49),
        color=colors_gay,
        scale=1.0,
        particles_per_tick=10,
    )
    particle_line(
        ticks_delay=10,
        ticks_total=6,
        startpos=(-3, 71, 58),
        endpos=(-11, 89, 49),
        color=colors_gay,
        scale=1.0,
        particles_per_tick=10,
    )


def heart_sequence():
    particle_heart(
        ticks_delay=45,
        center=(7, 82, 44),
        width=10,
        speed=8,
        color=[1.0, 0.7, 1.0],
        scale=0.6,
        tilt=[0, -26, 0],
    )
    particle_heart(
        ticks_delay=80,
        center=(-6, 76, 55),
        width=10,
        speed=8,
        color=[0.95, 0.0, 0.5],
        scale=0.6,
        tilt=[0, 28, 0],
    )
    particle_heart(
        ticks_delay=140,
        center=(19, 78, 60),
        width=10,
        speed=8,
        color=[1.0, 0.0, 0.6],
        scale=0.6,
        tilt=[0, -35, 0],
    )
    particle_heart(
        ticks_delay=180,
        center=(-15, 75, 62),
        width=10,
        speed=8,
        color=[1.0, 0.0, 0.6],
        scale=0.6,
        tilt=[0, 30, 0],
    )

    particle_heart(
        ticks_delay=475,
        center=(-12, 78, 55),
        width=10,
        speed=8,
        color=[1.0, 0.0, 0.5],
        scale=0.8,
        tilt=[17, 15, 0],
    )
    particle_heart(
        ticks_delay=475,
        center=(12, 78, 55),
        width=10,
        speed=8,
        color=[1.0, 0.3, 0.5],
        scale=0.8,
        tilt=[17, -15, 0],
    )
    particle_heart(
        ticks_delay=510,
        center=(14, 80, 62),
        width=10,
        speed=8,
        color=[1.0, 0.1, 0.6],
        scale=0.6,
        tilt=[17, 13, 0],
    )
    particle_heart(
        ticks_delay=520,
        center=(-13, 80, 61),
        width=10,
        speed=8,
        color=[1.0, 0.1, 0.6],
        scale=0.6,
        tilt=[14, 12, 0],
    )
    particle_heart(
        ticks_delay=520,
        center=(14, 78, 48),
        width=10,
        speed=8,
        color=[1.0, 0.15, 0.5],
        scale=0.6,
        tilt=[17, -14, 0],
    )
    particle_heart(
        ticks_delay=530,
        center=(-13, 78, 48),
        width=10,
        speed=8,
        color=[0.9, 0.15, 0.4],
        scale=0.6,
        tilt=[15, 14, 0],
    )

    for i in range(0, 15):
        particle_heart(
            ticks_delay=710 + i * 40,
            center=(
                random.uniform(-15, 15),
                random.uniform(75, 85),
                random.uniform(45, 65),
            ),
            width=10,
            speed=8,
            color=[
                random.uniform(0.9, 1.0),
                random.uniform(0.0, 0.15),
                random.uniform(0.3, 0.55),
            ],
            scale=random.uniform(0.5, 0.8),
            tilt=[random.uniform(0, 20), random.uniform(-15, 15), 0],
        )


def multi_spirals_sequence():
    particle_spiral_tapered(
        ticks_delay=60,
        center=(-10, 70, 65),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_trans[::-1],
        tilt=[180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=120,
        center=(11, 69, 64),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_bi[::-1],
        tilt=[180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=240,
        center=(10, 71, 48),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_lesbian[::-1],
        tilt=[180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=320,
        center=(-13, 73, 45),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_gay[::-1],
        tilt=[180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=620,
        center=(4, 71, 52),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_pan[::-1],
        tilt=[180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=620,
        center=(-4, 71, 52),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_bi[::-1],
        tilt=[180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=640,
        center=(10, 71, 47),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_mlm[::-1],
        tilt=[180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=640,
        center=(-10, 71, 47),
        top_radius=0.3,
        bottom_radius=4.0,
        height=15.0,
        steps=30,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_lesbian[::-1],
        tilt=[180.0, 0.0, 0.0],
    )

    particle_spiral_tapered(
        ticks_delay=800,
        center=(0, 90, 64),
        top_radius=1.0,
        bottom_radius=12.0,
        height=20.0,
        steps=50,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_gay[::-1],
        tilt=[0.0, 0.0, 0.0],
    )

    particle_spiral_tapered(
        ticks_delay=800,
        center=(0, 90, 64),
        top_radius=1.0,
        bottom_radius=12.0,
        height=20.0,
        steps=50,
        repeats=16,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_gay[::-1],
        tilt=[0.0, 0.0, 0.0],
    )


def firework_sequence():
    middle_part(0)
    fireworks_creeper(40, air7, [0.8, 0.0, 0.8])

    random_fireworks(50, count=20, delay=6)
    random_fireworks(80, count=25, delay=2)
    random_fireworks(100, count=40, delay=8)
    random_fireworks(350, count=25, delay=2)
    random_fireworks(550, count=70, delay=8)
    random_fireworks(700, count=25, delay=2)
    random_fireworks(900, count=25, delay=2)
    random_fireworks(950, count=45, delay=8)
    random_fireworks(1200, count=25, delay=2)

    arc_random(340)
    arc_random(650)
    arc_random(1200)

    circle_random(200)
    circle_random(400)
    circle_random(780)
    circle_random(1200)

    arc_part(60)
    arc_part(250)
    arc_part(850)
    arc_part(1250)

    middle_part(200)
    middle_part(700)
    middle_part(150)


def shooting_lines_sequence():
    shooting_lines_random(50, count=7, delay=1)
    shooting_lines_random(50, count=7, delay=2)

    shooting_lines_random(200, count=30, delay=3)
    shooting_lines_random(520, count=30, delay=1)
    shooting_lines_random(520, count=30, delay=1)
    shooting_lines_random(550, count=30, delay=2)
    shooting_lines_random(800, count=30, delay=3)
    shooting_lines_random(1100, count=30, delay=3)
    shooting_lines_random(1250, count=30, delay=2)


def stand_sequence():
    stands_all(0, 50)
    stands_all(450, 50)
    stands_all(900, 50)


def big_spirals_sequence():
    particle_spiral_tapered(
        ticks_delay=0,
        center=(0, 73, 78),
        top_radius=10.0,
        bottom_radius=3.0,
        height=38.0,
        steps=60,
        repeats=30,
        repeat_delay=6,
        revolve_times=6.0,
        color=colors_gay,
        tilt=[90.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=1320,
        center=(0, 73, 40),
        top_radius=10.0,
        bottom_radius=5.0,
        height=38.0,
        steps=60,
        repeats=30,
        repeat_delay=6,
        revolve_times=6.0,
        color=colors_gay,
        tilt=[-90.0, 0.0, 0.0],
    )

    particle_spiral_tapered(
        ticks_delay=450,
        center=(0, 91, 60),
        top_radius=1.0,
        bottom_radius=20.0,
        height=10.0,
        steps=60,
        repeats=20,
        repeat_delay=3,
        revolve_times=4.0,
        color=colors_gay,
        tilt=[-25.0, 0.0, 0.0],
    )

    particle_spiral_tapered(
        ticks_delay=1100,
        center=(0, 73, 55),
        top_radius=10.0,
        bottom_radius=10.0,
        height=30.0,
        steps=50,
        repeats=20,
        repeat_delay=4,
        revolve_times=5.0,
        color=colors_gay,
        tilt=[-180.0, 0.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=1140,
        center=(0, 73, 55),
        top_radius=10.0,
        bottom_radius=10.0,
        height=30.0,
        steps=50,
        repeats=20,
        repeat_delay=4,
        revolve_times=5.0,
        color=colors_trans,
        tilt=[-180.0, 15.0, 0.0],
    )
    particle_spiral_tapered(
        ticks_delay=1180,
        center=(0, 73, 55),
        top_radius=10.0,
        bottom_radius=10.0,
        height=30.0,
        steps=50,
        repeats=20,
        repeat_delay=4,
        revolve_times=5.0,
        color=colors_lesbian,
        tilt=[-180.0, 30.0, 0.0],
    )


def laser_sequence():
    lasers(30, 20, 2)
    lasers(30, 20, 1)

    lasers(300, 20, 2)
    lasers(510, 20, 2)
    lasers(650, 20, 2)
    lasers(1100, 40, 2)
    lasers(1250, 20, 2)


# The fireworks themselves, mostly random with a few specific shapes like an arc and a circle
firework_sequence()
# The stands next to the road, these show pride flags
stand_sequence()

# Some lines at the start
shape_sequence()

# Hearts in the sky
heart_sequence()
# These are lines shooting up from points next to the roads, towards a random point in the sky, in a pride flag pattern
laser_sequence()
# Shooting lines in the sky like shooting stars
shooting_lines_sequence()

# Big ooo spiral ooo you like kissing boys you like boys youre a boykisser
big_spirals_sequence()
# Smaller pride spirals scattered around
multi_spirals_sequence()

# Write all the commands to files
write_function_files()
