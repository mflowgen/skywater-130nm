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
1. Edit `SKYWATER130_HOME` in `create_view_standard.py` to point to the top folder of the skywater-pdk repository.
2. When you run this script `python3 create_view_standard.py`, it will:
    - Copy `rtk-tech.lef` from `SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/tech/sky130_fd_sc_hd.tlef'`.
    - Copy `stdcells.lib` from `SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/timing/sky130_fd_sc_hd__tt_025C_1v80.lib'`.
    - Generate `stdcells.db` from `stdcells.lib`.
    - Generate `stdcells.lef` by concatenating the LEFs for all cells in `SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/cells/'` into a single file.
3. Next, go into the `generate_captable` folder, and follow the steps in its `README.md`. Generating captables takes several hours. This creates `rtk-typical.captable`.
4. Once you have the captable, you can generate a Milkyway library. Go into the `generate_milkyway` folder, and follow the steps in its `README.md`. This generates `stdcells.mwlib` and `rtk-tech.tf`.
5. `rtk-stream-out.map` is copied from ``.
6. `adk.tcl` is handwritten.