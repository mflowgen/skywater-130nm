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
stdcells.gds
rtk-stream-out.map
adk.tcl
calibre-drc-block.rule
calibre.layerprops
calibre-lvs.rule
```

# Steps
1. Edit `SKYWATER130_HOME` in `skywater_path.py` to point to the top folder of the skywater-pdk repository.
2. `python3 generate_rtk_lef.py` copies technology lef file into `rtk-tech.lef`. Edit this file to add these lines after the last metal layer, otherwise LEF generation in Innovus complains. Mentioned here: https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hd/pull/5.
```
LAYER OVERLAP
  TYPE OVERLAP ;
END OVERLAP

```
3. Go into the `generate_captable` folder, and follow the steps in its `README.md`. Generating captables takes several hours. This creates `rtk-typical.captable`.
4. With the current version of the lef file, Innovus gives an error: `**ERROR: (IMPLF-121):   You need to have cut layer after layer 'pwell'.`. Manually add the `licon` layer after `pwell` layer definition in `rtk-tech.lef`. Captable generation fails with this change, so we should do that earlier. This is really hacky, and should be fixed properly (https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hd/pull/5).
```
LAYER licon
  TYPE CUT ;
END licon 
```
5. First run `python3 generate_lib.py` to copy typical lib file from the PDK. Then go into the `generate_lib` folder, and follow the steps in its `README.md`, since the copied lib file doesn't work out of the box with commercial tools.
6. `python3 generate_sc_lef.py` generates `stdcells.lef` by concatenating the lef files for all cells in `SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/cells/'` into a single file.
7. Similary `python3 generate_spi.py` generates `stdcells.spi` by concatenating the spice files for all cells.
8. `python3 generate_cdl.py` generates `stdcells.cdl` by concatenating the cdl files for all cells.
9. `python3 generate_verilog.py` generates `stdcells.v` by concatenating the Verilog files for all cells.
10. Go into the `generate_db` folder, and follow the steps in its `README.md` to generate `stdcells.db`.
11. Go into the `generate_milkyway` folder, and follow the steps in its `README.md`. This generates `stdcells.mwlib` and `rtk-tech.tf`.
12. `python3 generate_gds.py` copies all standard cell GDS's into a `stdcellsgds` directory. This takes a while to complete. Then run the following command to create a merged GDS file.
```
module load calibre
/cad/mentor/2019.1/aoi_cal_2019.1_18.11/bin/calibredrv -a layout filemerge -indir stdcellsgds -out view-standard/stdcells.gds
```
13. `rtk-stream-out.map` is copied from https://foss-eda-tools.googlesource.com/skywater-pdk/libs/sky130_osu_sc/+/refs/heads/master/flow/pnr/streamOut.map.
14. `adk.tcl` is handwritten looking at the lef and lib files.
15. The final three calibre files are not available yet. We need to create some scripts that generate these files from the technology information in the PDK. 
16. As an alternative, we are using magic to check DRCs, and extract a SPICE netlist from the layout and netgen for LVS. Magic needs a `.magicrc` file to be in the folder from which magic is invoked, and a `.tech` file. Netgen also needs a setup file. We will get these files from the `open_pdks` repo.
```
cp /afs/ir.stanford.edu/class/ee272/PDKS/sky130A/libs.tech/magic/sky130A.magicrc view-standard/magicrc
cp /afs/ir.stanford.edu/class/ee272/PDKS/sky130A/libs.tech/magic/sky130A.tcl view-standard
cp /afs/ir.stanford.edu/class/ee272/PDKS/sky130A/libs.tech/magic/sky130A.tech view-standard
cp /afs/ir.stanford.edu/class/ee272/PDKS/sky130A/libs.tech/netgen/sky130A_setup.tcl view-standard/netgen-setup.tcl
```
