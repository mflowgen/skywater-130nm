# Generating Milkyway Library
First load the required module to run Milkyway:
```
module load base
module load mw/latest
```
Then run Milkyway with the `generate_milkyway.tcl` script:
```
Milkyway -tcl -nogui -galaxy -file generate_milkyway.tcl
```
`exit` Milkyway once it completes. Copy the files over to `view-standard`:
```
cp rtk-tech.tf ../view-standard/
cp -r stdcells.mwlib ../view-standard/
```
