from meta.utils import *
import math


def pick_color_at_fraction(color_param, fraction):
    """
    If 'color_param' is a single color [r,g,b], return it.
    If it's a list of colors, pick one based on 'fraction' (discrete segments).
    """
    # Single color check
    if not isinstance(color_param[0], (list, tuple)):
        return color_param  # single [r,g,b]

    # Multiple colors => discrete segment approach
    segment_count = len(color_param)
    idx = int(fraction * segment_count)
    if idx >= segment_count:
        idx = segment_count - 1
    return color_param[idx]


def rotate_xyz(x, y, z, tilt):
    """
    Rotates point (x,y,z) by tilt=[rx,ry,rz] degrees around the X, Y, and Z axes, in that order.
    """
    rx, ry, rz = [math.radians(a) for a in tilt]

    # Rotate around X
    x1 = x
    y1 = y * math.cos(rx) - z * math.sin(rx)
    z1 = y * math.sin(rx) + z * math.cos(rx)

    # Rotate around Y
    x2 = x1 * math.cos(ry) + z1 * math.sin(ry)
    y2 = y1
    z2 = -x1 * math.sin(ry) + z1 * math.cos(ry)

    # Rotate around Z
    x3 = x2 * math.cos(rz) - y2 * math.sin(rz)
    y3 = x2 * math.sin(rz) + y2 * math.cos(rz)
    z3 = z2

    return x3, y3, z3


def particle_line(
    ticks_delay: int,
    ticks_total: int,
    startpos: tuple,
    endpos: tuple,
    color,
    scale=1.0,
    particles_per_tick=10,
):
    """
    Schedules a line of particles from startpos to endpos over 'ticks_total' ticks,
    beginning at 'ticks_delay'.

    'color' can be a single [r,g,b] or a list of [r,g,b].
    If it's a list, the line is split into color segments along its length.
    """
    x1, y1, z1 = startpos
    x2, y2, z2 = endpos

    total_steps = ticks_total * particles_per_tick
    if total_steps < 1:
        return  # No steps

    line_points = []
    for i in range(total_steps):
        fraction = i / (total_steps - 1) if total_steps > 1 else 0
        px = x1 + fraction * (x2 - x1)
        py = y1 + fraction * (y2 - y1)
        pz = z1 + fraction * (z2 - z1)

        # Pick color for this fraction
        col = pick_color_at_fraction(color, fraction)
        line_points.append((px, py, pz, col))

    for tick_index in range(ticks_total):
        start_idx = tick_index * particles_per_tick
        end_idx = start_idx + particles_per_tick
        chunk = line_points[start_idx:end_idx]

        for px, py, pz, col in chunk:
            cmd = (
                f"particle dust{{color:[{col[0]:.2f},{col[1]:.2f},{col[2]:.2f}],scale:{scale}}} "
                f"{px:.3f} {py:.3f} {pz:.3f} 0 0 0 0 1"
            )
            scheduled_commands[ticks_delay + tick_index].append(cmd)


def particle_heart(
    ticks_delay: int,
    center: tuple,
    width: float,
    speed: int,
    color=[1.0, 0.7, 1.0],
    scale=1.0,
    tilt=[15.0, 0.0, 0.0],
):
    """
    Schedules a heart of particles centered at 'center',
    sized 'width' blocks across, visible for 'speed' ticks,
    tilted by [tiltX, tiltY, tiltZ] degrees, starting at 'ticks_delay'.
    """
    cx, cy, cz = center

    # Generate the raw 2D heart shape
    steps = 80
    raw_points = []
    for i in range(steps):
        t = 2 * math.pi * (i / (steps - 1))
        x = 16 * (math.sin(t) ** 3)
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )
        raw_points.append((x, y))

    # Normalize to [-1..1]
    xs = [p[0] for p in raw_points]
    ys = [p[1] for p in raw_points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    scale_x = 2.0 / (max_x - min_x) if max_x != min_x else 1
    scale_y = 2.0 / (max_y - min_y) if max_y != min_y else 1

    norm_points = []
    for rx, ry in raw_points:
        nx = (rx - min_x) * scale_x - 1
        ny = (ry - min_y) * scale_y - 1
        norm_points.append((nx, ny))

    # Scale the heart to the desired width
    size_factor = width / 2.0

    # Generate commands for each tick in 'speed'
    for tick_offset in range(speed):
        for x, y in norm_points:
            x_scaled = x * size_factor
            y_scaled = y * size_factor

            # Apply tilt
            x_rot, y_rot, z_rot = rotate_xyz(x_scaled, y_scaled, 0, tilt)
            x_final = cx + x_rot
            y_final = cy + y_rot
            z_final = cz + z_rot

            cmd = (
                f"particle dust{{color:[{color[0]:.2f},{color[1]:.2f},{color[2]:.2f}],scale:{scale}}} "
                f"{x_final:.3f} {y_final:.3f} {z_final:.3f} 0 0 0 0 1"
            )
            scheduled_commands[ticks_delay + tick_offset].append(cmd)


def particle_spiral_tapered(
    ticks_delay: int,
    center: tuple,
    top_radius: float = 10.0,
    bottom_radius: float = 25.0,
    height: float = 10.0,
    steps: int = 60,
    repeats: int = 20,
    repeat_delay: int = 3,
    revolve_times: float = 4.0,
    color=[[1.0, 0.0, 0.0]],
    tilt=[15.0, 0.0, 0.0],
):
    """
    Creates a tapered spiral from 'top_radius' to 'bottom_radius' over 'height':
      - 8 streams around a circle
      - Each stream descends from top to bottom over 'steps' ticks
      - revolve_times controls horizontal revolutions
      - Repeated 'repeats' times, each separated by 'repeat_delay' ticks
      - 'color' can be single or multiple [r,g,b] arrays
      - 'tilt' is [rx, ry, rz] in degrees for the entire shape
    """
    cx, cy, cz = center
    streams = 8

    for r in range(repeats):
        start_tick = ticks_delay + r * repeat_delay

        for s in range(steps):
            frac = s / float(steps - 1) if steps > 1 else 0
            current_radius = top_radius + frac * (bottom_radius - top_radius)
            y_pos = cy - frac * height

            # Color at this fraction
            col = pick_color_at_fraction(color, frac)

            # revolve_times full rotations across 0..1
            step_angle = revolve_times * 2 * math.pi * frac

            for i in range(streams):
                base_angle = i * (2 * math.pi / streams)
                angle = base_angle + step_angle

                x_offset = current_radius * math.cos(angle)
                z_offset = current_radius * math.sin(angle)

                # Shift relative to center, apply tilt
                x_unrotated = x_offset
                y_unrotated = y_pos - cy
                z_unrotated = z_offset

                x_rot, y_rot, z_rot = rotate_xyz(
                    x_unrotated, y_unrotated, z_unrotated, tilt
                )

                # Translate back to world coords
                x_final = cx + x_rot
                y_final = cy + y_rot
                z_final = cz + z_rot

                cmd = (
                    f"particle dust{{color:[{col[0]:.2f},{col[1]:.2f},{col[2]:.2f}],scale:1.0}} "
                    f"{x_final:.3f} {y_final:.3f} {z_final:.3f} 0 0 0 0 1"
                )
                scheduled_commands[start_tick + s].append(cmd)
