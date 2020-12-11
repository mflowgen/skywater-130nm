# Setup

This repository converts the SkyWater 130 nm PDK into the format required by mflowgen for running a digital flow. mflowgen requires the following files in `view_standard` directory (for now, we will perform the setup for only regular VT cells, in typical corner):
```
rtk-tech.lef
adk.tcl
rtk-typical.captable
rtk-max.tluplus
rtk-min.tluplus
rtk-stream-out.map

rtk-tech.tf
rtk-tluplus.map
stdcells.cdl
stdcells.lib
stdcells.db
stdcells.gds
stdcells.lef
stdcells-lpe.spi
stdcells.mwlib
stdcells.v
calibre-drc-block.rule
calibre.layerprops
calibre-lvs.rule
```
0. 
1. `rtk-tech.lef`: 
