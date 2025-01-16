from effects.fireworks import *
from meta.values import *


def stand_flag_trans(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_trans):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_gay(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_gay):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_bi(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_bi):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_ace(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_ace):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_aro(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_aro):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_lesbian(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_lesbian):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_mlm(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_mlm):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_pan(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_pan):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stand_flag_enby(ticks_delay):
    intervals = 3
    for idx, c in enumerate(colors_enby):
        fireworks_burst(
            ticks_delay + intervals * idx, coords=globals()[f"stand{idx+1}"], color=c
        )


def stands_all(ticks_delay, delay):
    stand_flag_gay(ticks_delay + delay * 0)
    stand_flag_trans(ticks_delay + delay * 1)
    stand_flag_bi(ticks_delay + delay * 2)
    stand_flag_ace(ticks_delay + delay * 3)
    stand_flag_lesbian(ticks_delay + delay * 4)
    stand_flag_aro(ticks_delay + delay * 5)
    stand_flag_pan(ticks_delay + delay * 6)
    stand_flag_enby(ticks_delay + delay * 7)
    stand_flag_mlm(ticks_delay + delay * 8)
