# Setup

This repository converts the SkyWater 130 nm PDK into the format required by mflowgen for running a digital flow. mflowgen requires the following files in `view_standard` directory (for now, we will perform the setup for only regular VT cells, in typical corner). We will generate them in this order:
```
rtk-tech.lef
stdcells.lib
stdcells.lef
stdcells.spi
stdcells.cdl
stdcells.v
stdcells.db
stdcells.mwlib
rtk-tech.tf
rtk-typical.captable
rtk-stream-out.map
adk.tcl
stdcells.gds
calibre-drc-block.rule
calibre.layerprops
calibre-lvs.rule
```

# Steps
1. Edit `SKYWATER130_HOME` in `skywater_path.py` to point to the top folder of the skywater-pdk repository.
With the current version of the lef file, Innovus gives an error: `**ERROR: (IMPLF-121):   You need to have cut layer after layer 'pwell'.`. Manually comment the nwell and pweel layers for now, since they don't affect digital P&R.
2. `python3 generate_rtk_lef.py` copies technology lef file into `rtk-tech.lef`.
3. First run `python3 generate_lib.py` to copy typical lib file from the PDK. Then go into the `generate_lib` folder, and follow the steps in its `README.md`, since the copied lib file doesn't work out of the box with commercial tools.
4. `python3 generate_sc_lef.py` generates `stdcells.lef` by concatenating the lef files for all cells in `SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/cells/'` into a single file.
5. Similary `python3 generate_spi.py` generates `stdcells.spi` by concatenating the spice files for all cells.
6. `python3 generate_cdl.py` generates `stdcells.cdl` by concatenating the cdl files for all cells.
7. `python3 generate_verilog.py` generates `stdcells.v` by concatenating the Verilog files for all cells.
8. Go into the `generate_db` folder, and follow the steps in its `README.md` to generate `stdcells.db`.
9. Go into the `generate_milkyway` folder, and follow the steps in its `README.md`. This generates `stdcells.mwlib` and `rtk-tech.tf`.
10. Go into the `generate_captable` folder, and follow the steps in its `README.md`. Generating captables takes several hours. This creates `rtk-typical.captable`.
11. `rtk-stream-out.map` is copied from https://foss-eda-tools.googlesource.com/skywater-pdk/libs/sky130_osu_sc/+/refs/heads/master/flow/pnr/streamOut.map.
12. `adk.tcl` is handwritten looking at the lef and lib files.
13. The final three calibre files are not available yet. We need to create some scripts that generate these files from the technology information in the PDK.