# Generates db file
# Author: Charles Tsao

# Generate db file using lc_shell
lc_shell -f lc_shell_gen_db.tcl

cp $TOP/generate_db/sky130_fd_sc_hd__tt_025C_1v80.db $TOP/view-standard/stdcells.db
