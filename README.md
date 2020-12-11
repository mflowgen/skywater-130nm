# Setup

This repository converts the SkyWater 130 nm PDK into the format required by mflowgen for running a digital flow. mflowgen requires the following files in `view_standard` directory (for now, we will perform the setup for only regular VT cells, in typical corner):
```
adk.tcl
calibre-drc-antenna.rule
calibre-drc-block.rule
calibre-drc-chip.rule
calibre-fill.rule
calibre.layerprops
calibre-lvs.rule
calibre-lvs-devices.cdl
calibre-lvs-hcells.inc
rtk-typical.captable
rtk-max.tluplus
rtk-min.tluplus
rtk-stream-out.map
rtk-tech.lef
rtk-tech.tf
rtk-tluplus.map
stdcells-bc.db
stdcells.cdl
stdcells.db
stdcells.gds
stdcells.lef
stdcells.lib
stdcells-lpe.spi
stdcells.mwlib
stdcells.v
```