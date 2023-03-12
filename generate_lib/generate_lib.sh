# Generates lib file and performs hotfixes for adk
# Author: Charles Tsao

export lib_file=$TOP/generate_lib/sky130_fd_sc_hd__tt_025C_1v80.lib
# Generate lib file
# cp $SKYWATER130_HOME/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib $lib_file
python $TOP/generate_lib/generate_lib.py

process_lib() {
    # Hotfix for issue #183
    lines=$(grep -n 'sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap' $1 | cut -f1 -d:)
    offset=0
    for line in $lines; do
        line=$(($line + 22 + offset))
        sed -i "$line a \\
        pg_pin (\"VNB\") {\\
            pg_type : \"pwell\";\\
            physical_connection : \"device_layer\";\\
            voltage_name : \"VNB\";\\
        }" $1
        offset=$(($offset + 5))
    done
    offset=0
    lines=$(grep -n 'sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap' $1 | cut -f1 -d:)
    for line in $lines; do
        line=$(($line + 26 + offset))
        sed -i "$line a \\
        pg_pin (\"VNB\") {\\
            pg_type : \"pwell\";\\
            physical_connection : \"device_layer\";\\
            voltage_name : \"VNB\";\\
        }" $1
        offset=$(($offset + 5))
    done
}

process_lib $lib_file

lc_shell -f lc_shell_gen_lib.tcl

cp $lib_file $TOP/generate_db
cp $lib_file $TOP/view-standard/stdcells.lib
