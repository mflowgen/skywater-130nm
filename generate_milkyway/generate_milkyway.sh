# Generates Milkyway file
# Author: Charles Tsao

# Generate Milkyway file using generate_milkyway.tcl
Milkyway -tcl -nogui -galaxy -file generate_milkyway.tcl & exit

cp $TOP/generate_milkyway/rtk-tech.tf $TOP/view-standard/
cp -r $TOP/generate_milkyway/stdcells.mwlib $TOP/view-standard/
