from shutil import copyfile
import os

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
TOP = os.environ['TOP']
LIB = TOP + '/generate_lib/sky130_fd_sc_hd__tt_025C_1v80.lib'

copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib', LIB)

with open(LIB, 'r') as f:
    fdata = f.read()

# Hotfix for issue #183
fdata = fdata.replace(
"""
            internal_node : "M0";
            related_ground_pin : "VNB";
""",
"""
            internal_node : "M0";
            related_ground_pin : "VGND";
"""
)

with open(LIB, 'w') as f:
    f.write(fdata)
