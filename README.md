# Setup

This repository converts the SkyWater 130 nm PDK into the format required by mflowgen for running a digital flow. mflowgen requires the following files in `view_standard` directory (for now, we will perform the setup for only regular VT cells, in typical corner). Once complete, your folder should have the following:
```
adk.tcl
calibre-drc-block.rule
calibre.layerprops
calibre-lvs.rule
magicrc
netgen_setup.tcl
primitives.v
rtk-stream-out.map
rtk-tech.lef
rtk-tech.tf
rtk-typical.captable
stdcells.cdl
stdcells.db
stdcells.gds
stdcells.lef
stdcells.lib
stdcells.mwlib/ # Directory
stdcells.spi
stdcells.v
```

All of the steps below are automated by scripts in their respective folders. The python and/or shell script can be modified to automate hotfixes as the sky130A pdk is updated.

Running `make all` will build the entire adk.

# Steps
1. Edit the environment variables in `setenv.csh` to point to the top folder of your PDK repository and open_pdks (or volare) generated sky130A files.
2. `make rtk_lef` copies the technology lef file into `rtk-tech.lef`. LEF generation in Innovus requires an OVERLAP layer, and a cut layer is required between the non-routing layers (nwell/pwell/poly) and local interconnect. `generate_rtk_lef/generate_rtk_lef.sh` performs the hotfixes documented here: https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hd/pull/5.
3. `make captable` creates `rtk-typical.captable`. This takes several hours!
4. `make lib` copies the typical lib file from open_pdks. Note that the copied lib file does not work out-of-box with the commercial tools. Hotfixes are documented in the `generate_lib` folder's `README.md`.
5. `make sc_lef` generates `stdcells.lef` by copying the open_pdks version.
6. `make spi` generates `stdcells.spi` by copying the open_pdks version.
7. `make cdl` generates `stdcells.cdl` by copying the open_pdks version.
8. `make verilog` generates `stdcells.v` by copying the open_pdks stdcells and primitives verilog files.
9. `make db` generates `stdcells.db` using Library Compiler's `lc_shell`.
10. `make milkyway` generates `stdcells.mwlib` and `rtk-tech.tf` following the steps in `generate_milkyway/README.md`.
11. `make gds` generates `stdcells.gds` by copying the open_pdks version.
12. `rtk-stream-out.map` in the `view-standard` directory is copied from https://foss-eda-tools.googlesource.com/skywater-pdk/libs/sky130_osu_sc/+/refs/heads/master/flow/pnr/streamOut.map.
13. `adk.tcl` is handwritten looking at the lef and lib files.
14. The final files relate to Calibre and Magic to Check DRC and LVS:
    - The final three calibre files are not available yet. We need to create some scripts that generate these files from the technology information in the PDK. 
    - As an alternative, we are using magic to check DRCs, and extract a SPICE netlist from the layout and netgen for LVS. Magic needs a `.magicrc` file to be in the folder from which magic is invoked. Netgen also needs a setup file. These files are obtained by running `make magic`, which executes the two shell commands below:
```
cp ${SKYWATER130_HOME}/libs.tech/magic/sky130A.magicrc view-standard/magicrc
cp ${SKYWATER130_HOME}/libs.tech/netgen/sky130A_setup.tcl view-standard/netgen_setup.tcl
```
