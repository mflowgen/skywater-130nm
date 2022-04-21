# Generates verilog file
# Author: Charles Tsao

# Generate verilog file
python $TOP/generate_verilog/generate_verilog.py

sed -i 's/`default_nettype none//g' $TOP/view-standard/primitives.v
