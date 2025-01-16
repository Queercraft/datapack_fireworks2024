import os

from __init__ import scheduled_commands
from effects.countdown import create_countdown_mcfunction_files
from meta.values import namespace, output_dir


def write_function_files():
    """
    Writes all scheduled commands into files named '_fireworks<tick>.mcfunction'.
    Also creates 'fireworks_start.mcfunction' to call the earliest scheduled tick.
    """
    os.makedirs(output_dir, exist_ok=True)
    all_ticks = sorted(scheduled_commands.keys())
    if not all_ticks:
        return

    create_countdown_mcfunction_files()

    # Master function that triggers the earliest tick
    start_file = os.path.join(output_dir, "fireworks.mcfunction")
    with open(start_file, "w") as f:
        f.write(f"function {namespace}:_fireworks{all_ticks[0]}\n")

    for i, tick in enumerate(all_ticks):
        fn_name = f"_fireworks{tick}.mcfunction"
        fn_path = os.path.join(output_dir, fn_name)

        with open(fn_path, "w") as f:
            for cmd in scheduled_commands[tick]:
                f.write(cmd + "\n")

        # Schedule next tick with correct delay
        if i < len(all_ticks) - 1:
            next_tick = all_ticks[i + 1]
            delay = next_tick - tick
            with open(fn_path, "a") as f:
                f.write(
                    f"schedule function {namespace}:_fireworks{next_tick} {delay}t\n"
                )

    # Infinite loop to keep the fireworks going
    # Cancel next loop with /schedule clear <namespace>:loop
    # Immediately stop with /function <namespace>:stop
    loop_file = os.path.join(output_dir, "loop.mcfunction")
    with open(loop_file, "w") as f:
        f.write(f"function {namespace}:fireworks\n")
        f.write(f"schedule function {namespace}:loop {all_ticks[-1]+10}t\n")

    stop_file = os.path.join(output_dir, "stop.mcfunction")
    with open(stop_file, "w") as f:
        f.write(f"schedule clear {namespace}:fireworks\n")
        f.write(f"schedule clear {namespace}:loop\n")
        f.write(f"schedule clear {namespace}:countdown\n")
        for i in range(11):
            f.write(f"schedule clear {namespace}:_countdown-{i}\n")
        for tick in all_ticks:
            f.write(f"schedule clear {namespace}:_fireworks{tick}\n")
