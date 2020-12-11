# Setup

This repository converts the SkyWater 130 nm PDK into the format required by mflowgen for running a digital flow. mflowgen requires the following files in `view_standard` directory (for now, we will perform the setup for only regular VT cells, in typical corner). We will generate them in this order:
```
    rtk-tech.lef
    stdcells.lib
    stdcells.db
    stdcells.lef
    rtk-typical.captable
    stdcells.mwlib
    rtk-tech.tf
stdcells.cdl
stdcells.gds
stdcells-lpe.spi
stdcells.v
calibre-drc-block.rule
calibre.layerprops
calibre-lvs.rule
    rtk-stream-out.map
    adk.tcl
```

# Steps
1. Edit `SKYWATER130_HOME` in `skywater_path.py` to point to the top folder of the skywater-pdk repository.
2. `python3 generate_rtk_lef.py` copies technology lef file into `rtk-tech.lef`.
3. `python3 generate_lib.py` copies typical lib file into `stdcells.lib`.
4. Go into the `generate_db` folder and run to generate `stdcells.db` from `stdcells.lib`.
5. `python3 generate_sc_lef.py` generates `stdcells.lef` by concatenating the lef files for all cells in `SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/cells/'` into a single file.
6. Go into the `generate_milkyway` folder, and follow the steps in its `README.md`. This generates `stdcells.mwlib` and `rtk-tech.tf`.
7. Go into the `generate_captable` folder, and follow the steps in its `README.md`. Generating captables takes several hours. This creates `rtk-typical.captable`.
8. `rtk-stream-out.map` is copied from https://foss-eda-tools.googlesource.com/skywater-pdk/libs/sky130_osu_sc/+/refs/heads/master/flow/pnr/streamOut.map.
9. `adk.tcl` is handwritten looking at the lef and lib files.