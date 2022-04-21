from glob import glob
# from utils import *
from shutil import copyfile
import os

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
TOP = os.environ['TOP']
CDL = TOP + '/view-standard/stdcells.cdl'

copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/cdl/sky130_fd_sc_hd.cdl', CDL)

# cell_dirs = glob(SKYWATER130_HOME + "/libraries/sky130_fd_sc_hd/latest/cells/*/")

# outfilename = 'view-standard/stdcells.cdl'
# infilenames = []

# for cell_dir in cell_dirs:
#     libname = cell_dir.split('/')[-5]
#     cellname = cell_dir.split('/')[-2]

#     # CDL file for each size
#     infilenames = infilenames + glob(cell_dir+libname+'__'+cellname+'_*.cdl')

# write_concat_file(outfilename, infilenames)


