from glob import glob
# from utils import *
from shutil import copyfile
import os

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
TOP = os.environ['TOP']
copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v', TOP + '/view-standard/stdcells.v')
copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/verilog/primitives.v', TOP + '/view-standard/primitives.v')

# cell_dirs = glob(SKYWATER130_HOME + "/libraries/sky130_fd_sc_hd/latest/cells/*/")

# outfilename = 'view-standard/stdcells.v'
# infilenames = []

# for cell_dir in cell_dirs:
#     libname = cell_dir.split('/')[-5]
#     cellname = cell_dir.split('/')[-2]

#     infilenames = infilenames + glob(cell_dir+libname+'__'+cellname+'_*.v')

# write_concat_file(outfilename, infilenames)
