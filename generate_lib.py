from shutil import copyfile
import os

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib', 'generate_lib/sky130_fd_sc_hd__tt_025C_1v80.lib')
