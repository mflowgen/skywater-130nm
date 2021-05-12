Generation of db file requires Library Compiler.
First load the modules to run this tool:
```
module load base
module load lc
```
Then start `lc_shell`:
```
lc_shell
```
Then in the lc_shell prompt, run:
```
read_lib sky130_fd_sc_hd__tt_025C_1v80.lib
```
After reading the library make sure that `lc_shell` prints the following message at the end. Otherwise, look for errors in the log and fix the lib file.
```
Technology library 'sky130_fd_sc_hd__tt_025C_1v80' read successfully
```
Finally, write out the library in db format:
```
write_lib "[get_object_name [get_libs]]" -format db -output sky130_fd_sc_hd__tt_025C_1v80.db
exit
```
Copy the db:
```
cp sky130_fd_sc_hd__tt_025C_1v80.db ../view-standard/stdcells.db
```
