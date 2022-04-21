Innovus has a utility called generateCapTbl which takes the technology LEF file and an ICT file and generates captables.

The ICT file is not available in the skywater-pdk repository. It is copied from this issue: https://github.com/google/skywater-pdk/issues/187#issuecomment-718312348 and put in skywater130.nominal.ict.

The below steps are covered in the `make captable` command, which calls `generate_captable.sh`.

First make sure the innovus module is loaded:
```
module load innovus
```
Then run:
```
generateCapTbl -ict skywater130.nominal.ict -lef ../view-standard/rtk-tech.lef -output rtk-typical.captable
```
This command takes several hours to run.
Finally copy the generated file to the adk view:
```
cp rtk-typical.captable ../view-standard
```
