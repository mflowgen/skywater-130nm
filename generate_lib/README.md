The lib file generated from the PDK does not work out of the box, and several changes are required.

1. For for db file generation:
* Swap `related_bias_pin : "VPB";` and `related_bias_pin : "VNB";` (This is an error in the lib files reported here: https://github.com/google/skywater-pdk/issues/288). 
* Swap `pg_type : "nwell";` and `pg_type : "pwell";`
* Fix all errors mentioned here : https://github.com/google/skywater-pdk/issues/183

2. There is a warning in DC: `Warning: The 'sky130_fd_sc_hd__macro_sparecell' cell in the 'sky130_fd_sc_hd__tt_025C_1v80' technology library does not have corresponding physical cell description. (PSYN-024)`, that causes an assertion to fail in mflowgen. So remove this cell manually from the lib.

Finally copy the lib file:
```
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../generate_db
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../view-standard/stdcells.lib
```
