The lib file generated from the PDK does not work out of the box, and several changes are required. These changes are automated by the `generate_lib.sh` and `generate_lib.py` scripts.

For for db file generation:
1. Fix the errors reported here: https://github.com/google/skywater-pdk/issues/288 .
* Swap `related_bias_pin : "VPB";` and `related_bias_pin : "VNB";`
```
sed -i 's/related_bias_pin : "VPB";/related_bias_pin : "VNBTEMP";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/related_bias_pin : "VNB";/related_bias_pin : "VPB";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/related_bias_pin : "VNBTEMP";/related_bias_pin : "VNB";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
```
* Swap `pg_type : "nwell";` and `pg_type : "pwell";`
```
sed -i 's/pg_type : "nwell";/pg_type : "pwelltemp";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/pg_type : "pwell";/pg_type : "nwell";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
sed -i 's/pg_type : "pwelltemp";/pg_type : "pwell";/g' sky130_fd_sc_hd__tt_025C_1v80.lib
```

2. Fix the errors mentioned here : https://github.com/google/skywater-pdk/issues/183. 
   1. The first error is in all sizes of `sky130_fd_sc_hd__dlclkp` and `sky130_fd_sc_hd__sdlclkp`. The `M0` pin incorrectly marks the `related_ground_pin` as `VNB`, but it needs to be `VGND`.
   2. The second error is in all sizes of `sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap` and `sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap`. `VNB` definition is missing.
       ```
       pg_pin ("VNB") {
           pg_type : "pwell";
           physical_connection : "device_layer";
           voltage_name : "VNB";
       }
       ```

3. There is a warning in DC: `Warning: The 'sky130_fd_sc_hd__macro_sparecell' cell in the 'sky130_fd_sc_hd__tt_025C_1v80' technology library does not have corresponding physical cell description. (PSYN-024)`, that causes an assertion to fail in mflowgen. So remove this cell manually from the lib.

4. If you want to check that you fixed all of the issues before leaving, run `lc_shell` and run:
```
read_lib sky130_fd_sc_hd__tt_025C_1v80.lib
```
If you see :
```
Technology library 'sky130_fd_sc_hd__tt_025C_1v80' read successfully
```
Then you (probably) correctly fixed all of the issues.

5. Finally copy the lib file:
```
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../generate_db
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../view-standard/stdcells.lib
```
