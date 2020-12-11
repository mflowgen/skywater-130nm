# Setup

This repository converts the SkyWater 130 nm PDK into the format required by mflowgen for running a digital flow. mflowgen requires the following files in `view_standard` directory (for now, we will perform the setup for only regular VT cells, in typical corner):
```
adk.tcl
rtk-typical.captable
rtk-max.tluplus
rtk-min.tluplus
rtk-stream-out.map
rtk-tech.lef
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

# Steps
1. Edit `SKYWATER130_HOME` in `create_view_standard.py` to point to the top folder of the skywater-pdk repository.
2. When you run this script `python3 create_view_standard.py`, it will:
    - Copy `rtk-tech.lef` from 
    - Copy `stdcells.lib` from 
