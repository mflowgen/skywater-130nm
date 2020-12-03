Innovus has a utility called generateCapTbl which takes the technology LEF file and an ICT file and generates captables.
First make sure that you load the innovus module:
```
bash
module load innovus
```
Then run:
```
generateCapTbl -ict skywater130.nominal.ict -lef ../view-standard/rtk-tech.lef -output rtk-typical.captable
```
This command takes several hours to run.
