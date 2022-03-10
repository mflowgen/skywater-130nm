from shutil import copyfile
import os

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/tech/sky130_fd_sc_hd.tlef', 'view-standard/rtk-tech.lef')
