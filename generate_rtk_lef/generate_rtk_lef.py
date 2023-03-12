from shutil import copyfile
import os

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
TOP = os.environ['TOP']
copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/techlef/sky130_fd_sc_hd__nom.tlef', TOP + '/view-standard/rtk-tech.lef')
