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
1. Edit the environment variables in `setenv.csh` to point to the top folder of the skywater-pdk repository and open_pdks generated files.
2. `python3 generate_rtk_lef.py` copies technology lef file into `rtk-tech.lef`. LEF generation in Innovus requires OVERLAP layer, and a cut layer is required between the non-routing layers (nwell/pwell/poly) and local interconnect. Edit this file following the changes mentioned in this PR: https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hd/pull/5.
3. Go into the `generate_captable` folder, and follow the steps in its `README.md`. Generating captables takes several hours. This creates `rtk-typical.captable`.
4. Run `python3 generate_lib.py` to copy typical lib file from the open_pdks. Then go into the `generate_lib` folder, and follow the steps in its `README.md`, since the copied lib file doesn't work out of the box with commercial tools.
5. Run `python3 generate_sc_lef.py` to generate `stdcells.lef` by copying the open_pdks version.
6. Run `python3 generate_spi.py` to generate `stdcells.spi` by copying the open_pdks version.
7. Run `python3 generate_cdl.py` to generate `stdcells.cdl` by copying the open_pdks version.
8. Run `python3 generate_verilog.py` to generate `stdcells.v` by copying the open_pdks stdcells and primitives verilog files.
   - Gate-level VCS simulation fails with the error message `Identifier 'SET' has not been declared yet. If this error is not expected, please check if you have set \`default_nettype to none.` Temporarily fixing the issue by removing those statements from `primitives.v`.
   ```
   sed -i 's/`default_nettype none//g' view-stanfard/primitives.v
   ```
9. Go into the `generate_db` folder, and follow the steps in its `README.md` to generate `stdcells.db`.
10. Go into the `generate_milkyway` folder, and follow the steps in its `README.md`. This generates `stdcells.mwlib` and `rtk-tech.tf`.
11. Run `python3 generate_gds.py` to generate `stdcells.gds` by copying the open_pdks version.
12. `rtk-stream-out.map` in the `view-standard` directory is copied from https://foss-eda-tools.googlesource.com/skywater-pdk/libs/sky130_osu_sc/+/refs/heads/master/flow/pnr/streamOut.map.
13. `adk.tcl` is handwritten looking at the lef and lib files.
14. The final files relate to Calibre and Magic to Check DRC and LVS:
    - The final three calibre files are not available yet. We need to create some scripts that generate these files from the technology information in the PDK. 
    - As an alternative, we are using magic to check DRCs, and extract a SPICE netlist from the layout and netgen for LVS. Magic needs a `.magicrc` file to be in the folder from which magic is invoked. Netgen also needs a setup file. We will get these files from the open_pdks folder. 
```
cp ${SKYWATER130_HOME}/libs.tech/magic/sky130A.magicrc view-standard/magicrc
cp ${SKYWATER130_HOME}/libs.tech/netgen/sky130A_setup.tcl view-standard/netgen_setup.tcl
```
