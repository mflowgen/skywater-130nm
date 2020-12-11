from shutil import copyfile
from skywater_path import *

copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/tech/sky130_fd_sc_hd.tlef', 'view-standard/rtk-tech.lef')
