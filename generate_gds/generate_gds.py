from shutil import copyfile
from glob import glob
# from utils import *
import os 

SKYWATER130_HOME = os.environ['SKYWATER130_HOME']
copyfile(SKYWATER130_HOME + '/libs.ref/sky130_fd_sc_hd/gds/sky130_fd_sc_hd.gds', 'view-standard/stdcells.gds')

# cell_dirs = glob(SKYWATER130_HOME + "/libraries/sky130_fd_sc_hd/latest/cells/*/")

# if(~os.path.isdir("stdcellsgds")):
#     os.mkdir("stdcellsgds")

# infilenames = []

# for cell_dir in cell_dirs:
#     libname = cell_dir.split('/')[-5]
#     cellname = cell_dir.split('/')[-2]


#     infilenames = infilenames + glob(cell_dir+libname+'__'+cellname+'_*.gds')
    
#     for fname in infilenames:
#         copyfile(fname, 'stdcellsgds/'+fname.split('/')[-1])
