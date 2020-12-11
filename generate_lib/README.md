The lib file generated from the PDK does not work out of the box, and several changes are required.

1. For for db file generation:
* Remove `related_bias_pin : "VPB";`
* Remove `related_bias_pin : "VNB";`
* Remove `physical_connection : "device_layer";`
* Replace `pg_type : "nwell";` with `pg_type : "primary_ground";`
* Replace `pg_type : "pwell";` with `pg_type : "primary_power";`

2. Innovus could not recognize buffers for CTS. To fix this we have to make the following change in lib: make VNB and VPB lower case. 

Run the following commands to make all of the above changes:
```
sed -i 's/pg_type : "nwell";/pg_type : "primary_ground";/g' sky130_fd_sc_hd__tt_025C_1v80.lib 
sed -i 's/pg_type : "pwell";/pg_type : "primary_power";/g' sky130_fd_sc_hd__tt_025C_1v80.lib     
sed -i 's/related_bias_pin : "VPB";//g' sky130_fd_sc_hd__tt_025C_1v80.lib                                   
sed -i 's/related_bias_pin : "VNB";//g' sky130_fd_sc_hd__tt_025C_1v80.lib                                   
sed -i 's/physical_connection : "device_layer";//g' sky130_fd_sc_hd__tt_025C_1v80.lib    
sed -i 's/VPB/vpb/g' sky130_fd_sc_hd__tt_025C_1v80.lib                                                                                            
sed -i 's/VNB/vnb/g' sky130_fd_sc_hd__tt_025C_1v80.lib                                               
```

3. There is a warning in DC: `Warning: The 'sky130_fd_sc_hd__macro_sparecell' cell in the 'sky130_fd_sc_hd__tt_025C_1v80' technology library does not have corresponding physical cell description. (PSYN-024)`, that causes an assertion to fail in mflowgen. So remove this cell manually from the lib.

Finally copy the lib file:
```
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../generate_db
cp sky130_fd_sc_hd__tt_025C_1v80.lib ../view-standard/stdcells.lib
```
