from shutil import copyfile
from skywater_path import *

copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/timing/sky130_fd_sc_hd__tt_025C_1v80.lib', 'view-standard/stdcells.lib')
copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/timing/sky130_fd_sc_hd__tt_025C_1v80.lib', 'generate_db/sky130_fd_sc_hd__tt_025C_1v80.lib')
