from meta.values import namespace, output_dir

# Sorry this code sucks! just yoinked it from last years <3 works fine enough :3c


def create_countdown_mcfunction_files():
    # Countdown numbers and their corresponding colors
    countdown_info = {
        10: "green",
        9: "green",
        8: "green",
        7: "green",
        6: "green",
        5: "gold",
        4: "gold",
        3: "red",
        2: "red",
        1: "red",
        0: "white",  # Special case for "HAPPY NEW YEAR!"
    }

    # Create individual countdown files
    for number, color in countdown_info.items():
        text = "HAPPY NEW YEAR!" if number == 0 else str(number)
        bold = "true" if number == 0 else "false"
        content = (
            f"execute positioned 0 0 0 run title @a[distance=..250] title "
            f'{{"text":"{text}", "bold":{bold}, "color":"{color}"}}\n'
        )

        file_name = f"{output_dir}/_countdown-{number}.mcfunction"
        with open(file_name, "w") as file:
            file.write(content)

    # Create the main countdown file
    main_content = (
        "execute positioned 0 0 0 run title @a[distance=..250] times 5 10 5\n"
        f"function {namespace}:_countdown-10\n"
    )

    for i in range(9, 0, -1):
        main_content += (
            f"schedule function {namespace}:_countdown-{i} {10 - i}s append\n"
        )

    main_content += (
        "execute positioned 0 0 0 run title @a[distance=..250] times 5 60 5\n"
        f"schedule function {namespace}:_countdown-0 10s append\n"
        f"schedule function {namespace}:fireworks 10s append\n"
    )

    with open(f"{output_dir}/countdown.mcfunction", "w") as main_file:
        main_file.write(main_content)
