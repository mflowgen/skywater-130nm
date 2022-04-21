from glob import glob
from shutil import copyfile
# from utils import *
import os

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
TOP = os.environ['TOP']
SPI = TOP + '/view-standard/stdcells.spi'

copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/spice/sky130_fd_sc_hd.spice', SPI)

# cell_dirs = glob(SKYWATER130_HOME + "/libraries/sky130_fd_sc_hd/latest/cells/*/")

# outfilename = 'view-standard/stdcells.spi'
# infilenames = []

# for cell_dir in cell_dirs:
#     libname = cell_dir.split('/')[-5]
#     cellname = cell_dir.split('/')[-2]

#     # Spice file for each size
#     infilenames = infilenames + glob(cell_dir+libname+'__'+cellname+'_*.spice')

# write_concat_file(outfilename, infilenames)
