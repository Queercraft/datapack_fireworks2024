from effects.fireworks import *
from meta.values import *

import random


def random_fireworks(tick_delay, count=20, delay=3):
    for i in range(count):
        x = random.uniform(-30, 30)
        y = random.uniform(77, 110)
        z = random.uniform(70, 35)

        fireworks_random(
            ticks_delay=tick_delay + i * delay,
            coords=[(x, y, z)],
        )


def middle_part(tick_delay):
    fireworks_small_ball(tick_delay + 0, air1, colors_gay[0])
    fireworks_large_ball(tick_delay + 8, air2, colors_gay[1])
    fireworks_star(tick_delay + 16, air3, colors_gay[2])
    fireworks_small_ball(tick_delay + 24, air4, colors_gay[3])
    fireworks_star(tick_delay + 32, air5, colors_gay[4])
    fireworks_large_ball(tick_delay + 32, air6, colors_gay[5])


def arc_part(tick_delay):
    fireworks_small_ball(tick_delay + 0, arc1, colors_trans[2])
    fireworks_small_ball(tick_delay + 4, arc2, colors_trans[3])
    fireworks_small_ball(tick_delay + 8, arc3, colors_trans[4])
    fireworks_small_ball(tick_delay + 12, arc4, [0.6, 0.3, 0.2])
    fireworks_small_ball(tick_delay + 16, arc5, colors_gay[0])
    fireworks_small_ball(tick_delay + 20, arc6, colors_gay[1])
    fireworks_small_ball(tick_delay + 24, arc7, colors_gay[2])
    fireworks_small_ball(tick_delay + 28, arc8, colors_gay[3])
    fireworks_small_ball(tick_delay + 32, arc9, colors_gay[4])
    fireworks_small_ball(tick_delay + 36, arc10, colors_gay[5])
    fireworks_small_ball(tick_delay + 40, arc11, colors_bi[0])
    fireworks_small_ball(tick_delay + 44, arc12, colors_bi[2])
    fireworks_small_ball(tick_delay + 48, arc13, colors_bi[4])


def arc_random(tick_delay):
    fireworks_random(tick_delay + 0, arc1)
    fireworks_random(tick_delay + 6, arc13)
    fireworks_random(tick_delay + 12, arc2)
    fireworks_random(tick_delay + 18, arc12)
    fireworks_random(tick_delay + 24, arc3)
    fireworks_random(tick_delay + 30, arc11)
    fireworks_random(tick_delay + 36, arc4)
    fireworks_random(tick_delay + 42, arc10)
    fireworks_random(tick_delay + 48, arc5)
    fireworks_random(tick_delay + 54, arc9)
    fireworks_random(tick_delay + 60, arc6)
    fireworks_random(tick_delay + 66, arc8)
    fireworks_random(tick_delay + 72, arc7)


def circle_random(tick_delay):
    fireworks_random(tick_delay + 0, circle1)
    fireworks_random(tick_delay + 4, circle2)
    fireworks_random(tick_delay + 8, circle3)
    fireworks_random(tick_delay + 12, circle4)
    fireworks_random(tick_delay + 16, circle5)
    fireworks_random(tick_delay + 20, circle6)
    fireworks_random(tick_delay + 24, circle7)
    fireworks_random(tick_delay + 28, circle8)
