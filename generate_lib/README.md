The lib file generated from the PDK does not work out of the box, and several changes are required.

1. For for db file generation:
* Swap `related_bias_pin : "VPB";` and `related_bias_pin : "VNB";` (This is an error in the lib files reported here: https://github.com/google/skywater-pdk/issues/288).
```
sed -i 's/related_bias_pin : "VPB";/related_bias_pin : "VNBTEMP";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/related_bias_pin : "VNB";/related_bias_pin : "VPB";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/related_bias_pin : "VNBTEMP";/related_bias_pin : "VNB";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
```
* Swap `pg_type : "nwell";` and `pg_type : "pwell";`
Perhaps there is an easier way, but I used sed:
```
sed -i 's/pg_type : "nwell";/pg_type : "pwelltemp";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/pg_type : "pwell";/pg_type : "nwell";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/pg_type : "pwelltemp";/pg_type : "pwell";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
```
* Fix the errors mentioned here : https://github.com/google/skywater-pdk/issues/183. The first error exists in several cells: all sizes of `sky130_fd_sc_hd__dlclkp` and `sky130_fd_sc_hd__sdlclkp`. The second error occurs in all sizes of `sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap` and `sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap`.

2. There is a warning in DC: `Warning: The 'sky130_fd_sc_hd__macro_sparecell' cell in the 'sky130_fd_sc_hd__tt_025C_1v80' technology library does not have corresponding physical cell description. (PSYN-024)`, that causes an assertion to fail in mflowgen. So remove this cell manually from the lib.

Finally copy the lib file:
```
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../generate_db
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../view-standard/stdcells.lib
```
