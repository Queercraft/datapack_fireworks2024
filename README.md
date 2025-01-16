# Queercraft LIVE New Year's Eve 2024 fireworks

This repository contains the code used to generate the datapack used to create the fireworks show on Queercraft LIVE's New Year's Eve 2024 event.  

[![Recording of the fireworks show](https://img.youtube.com/vi/aT17biO12kg/0.jpg)](https://www.youtube.com/watch?v=aT17biO12kg)

## Repository
To generate the fireworks, run the `generate.py` file.  

The `effects/` package contains basic code for using fireworks and particles.  
The `parts/` package strings these together for more complex effects using them.
The `generate.py` file sequences these into the full fireworks show.
The `meta/` package contains information and utilities used across the pack.
The `meta/values.py` file contains configuration values used in the pack (such as coordinates).

## Datapack installation
Get the latest release from the [releases page](https://github.com/Queercraft/datapack_fireworks2024/releases) and install it in your world's `datapacks` folder.
To build it locally, run the `generate.py` file in this directory. This entire repository can be dragged into the world `datapacks` folder or just `data` and `pack.mcmeta` can be compressed into a zip for installation.  

## Datapack usage
#### Start 10 second countdown, followed by fireworks
`/function fireworks2024:countdown`

#### Just immediately start the fireworks
`/function fireworks2024:fireworks`

#### Start fireworks and loop them after it finishes
`/function fireworks2024:loop`

#### Cancel the next loop
`/schedule clear fireworks2024:loop`

#### Immediately stop all fireworks & cancel next loop if applicable
`/function fireworks2024:stop`