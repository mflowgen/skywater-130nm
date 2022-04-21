# Generates lib file and performs hotfixes for adk
# Author: Charles Tsao

export lib_file=$TOP/generate_lib/sky130_fd_sc_hd__tt_025C_1v80.lib
# Generate lib file
# cp $SKYWATER130_HOME/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib $lib_file
python $TOP/generate_lib/generate_lib.py

# Hotfix for issue #288
# Swap related_bias_pin VPB and VNB
sed -i 's/related_bias_pin : "VPB";/related_bias_pin : "VNBTEMP";/g' $lib_file
sed -i 's/related_bias_pin : "VNB";/related_bias_pin : "VPB";/g' $lib_file
sed -i 's/related_bias_pin : "VNBTEMP";/related_bias_pin : "VNB";/g' $lib_file

# Swap pg_type nwell and pwell
sed -i 's/pg_type : "nwell";/pg_type : "pwelltemp";/g' $lib_file
sed -i 's/pg_type : "pwell";/pg_type : "nwell";/g' $lib_file
sed -i 's/pg_type : "pwelltemp";/pg_type : "pwell";/g' $lib_file

# Hotfix for issue #183
sed -i '82150 a \
        pg_pin ("VNB") {\
            pg_type : "pwell";\
            physical_connection : "device_layer";\
            voltage_name : "VNB";\
        }' $lib_file
sed -i '82289 a \
        pg_pin ("VNB") {\
            pg_type : "pwell";\
            physical_connection : "device_layer";\
            voltage_name : "VNB";\
        }' $lib_file
sed -i '82428 a \
        pg_pin ("VNB") {\
            pg_type : "pwell";\
            physical_connection : "device_layer";\
            voltage_name : "VNB";\
        }' $lib_file
sed -i '82710 a \
        pg_pin ("VNB") {\
            pg_type : "pwell";\
            physical_connection : "device_layer";\
            voltage_name : "VNB";\
        }' $lib_file
sed -i '82849 a \
        pg_pin ("VNB") {\
            pg_type : "pwell";\
            physical_connection : "device_layer";\
            voltage_name : "VNB";\
        }' $lib_file
sed -i '82988 a \
        pg_pin ("VNB") {\
            pg_type : "pwell";\
            physical_connection : "device_layer";\
            voltage_name : "VNB";\
        }' $lib_file

# Remove sparecell
sed -i '83101, 83135d' $lib_file

lc_shell -f lc_shell_gen_lib.tcl

cp $lib_file $TOP/generate_db
cp $lib_file $TOP/view-standard/stdcells.lib
