# Setup

This repository converts the SkyWater 130 nm PDK into the format required by mflowgen for running a digital flow. mflowgen requires the following files in `view_standard` directory (for now, we will perform the setup for only regular VT cells, in typical corner). Once complete, your folder should have the following:
```
stdcells.mwlib/ #Directory
adk.tcl
calibre-drc-block.rule
calibre.layerprops
calibre-lvs.rule
rtk-stream-out.map
rtk-tech.lef
rtk-tech.tf
rtk-typical.captable
stdcells.cdl
stdcells.db
stdcells.gds
stdcells.lib
stdcells.lef
stdcells.spi
stdcells.v
```

# Steps
1. Edit `SKYWATER130_HOME` in `skywater_path.py` to point to the top folder of the skywater-pdk repository.
2. `python3 generate_rtk_lef.py` copies technology lef file into `rtk-tech.lef`. LEF generation in Innovus requires OVERLAP layer, and a cut layer is required between the non-routing layers (nwell/pwell/poly) and local interconnect. Edit this file following the changes mentioned in this PR: https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hd/pull/5.
3. Go into the `generate_captable` folder, and follow the steps in its `README.md`. Generating captables takes several hours. This creates `rtk-typical.captable`.
4. Run `python3 generate_lib.py` to copy typical lib file from the PDK. Then go into the `generate_lib` folder, and follow the steps in its `README.md`, since the copied lib file doesn't work out of the box with commercial tools.
5. Run `python3 generate_sc_lef.py` to generate `stdcells.lef` by concatenating the .magic.lef files for all cells in `SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/cells/'` into a single file.
6. Run `python3 generate_spi.py` to generate `stdcells.spi` by concatenating the spice files for all cells.
7. Run `python3 generate_cdl.py` to generate `stdcells.cdl` by concatenating the cdl files for all cells.
8. Run `python3 generate_verilog.py` to generate `stdcells.v` by concatenating the Verilog files for all cells.
9. Go into the `generate_db` folder, and follow the steps in its `README.md` to generate `stdcells.db`.
10. Go into the `generate_milkyway` folder, and follow the steps in its `README.md`. This generates `stdcells.mwlib` and `rtk-tech.tf`.
11. Run `python3 generate_gds.py` to copy all standard cell GDS's into a `stdcellsgds` directory. This takes a while (minutes) to complete. Then run the following command to create a merged GDS file.
```
module load calibre
/cad/mentor/2019.1/aoi_cal_2019.1_18.11/bin/calibredrv -a layout filemerge -indir stdcellsgds -out view-standard/stdcells.gds
```
12. `rtk-stream-out.map` in the `view-standard` directory is copied from https://foss-eda-tools.googlesource.com/skywater-pdk/libs/sky130_osu_sc/+/refs/heads/master/flow/pnr/streamOut.map.
13. `adk.tcl` is handwritten looking at the lef and lib files.
14. The final files relate to Calibre and Magic to Check DRC and LVS:
    - The final three calibre files are not available yet. We need to create some scripts that generate these files from the technology information in the PDK. 
    - As an alternative, we are using magic to check DRCs, and extract a SPICE netlist from the layout and netgen for LVS. Magic needs a `.magicrc` file to be in the folder from which magic is invoked, and a `.tech` file. Netgen also needs a setup file. We will get these files from the `open_pdks` repo. 
```
set OPEN_PDKS_ROOT = /farmshare/classes/ee/272/PDKs/share/pdk
cp ${OPEN_PDKS_ROOT}/sky130A/libs.tech/magic/sky130A.magicrc view-standard/magicrc
cp ${OPEN_PDKS_ROOT}/sky130A/libs.tech/magic/sky130A.tcl view-standard
cp ${OPEN_PDKS_ROOT}/sky130A/libs.tech/magic/sky130A.tech view-standard
cp ${OPEN_PDKS_ROOT}/sky130A/libs.tech/netgen/sky130A_setup.tcl view-standard/netgen-setup.tcl
```
TODO: A new Singularity container will be built after the quarter to align the paths in the native farmshare machine and the container. Will need to update this path.
There may be a way to skip the `share/pdk` directories when generating with `open_pdks`. We cannot simply move the directory since the path is coded in the files. We should fix this next time.
