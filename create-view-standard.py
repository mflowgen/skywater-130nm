from glob import glob
from shutil import copyfile

def write_concat_lef_file(outfilename, infilenames):
    first_file = True
    with open(outfilename, 'w') as outfile:
        for fname in infilenames:
            with open(fname) as infile:
                start_macro = False
                end_macro = False
                for line in infile:
                    # Only write lines between MACRO ... END macro
                    if line.startswith('MACRO'):
                        start_macro = True
                    if line.startswith('END LIBRARY'):
                        end_macro = True
                    if (first_file and not end_macro) or (not first_file and (start_macro and not end_macro)):
                        outfile.write(line)
                first_file = False
        outfile.write('END LIBRARY')


def write_concat_file(outfilename, infilenames):
    with open(outfilename, 'w') as outfile:
        for fname in infilenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

SKYWATER130_HOME = '../skywater-pdk'
cell_dirs = glob(SKYWATER130_HOME + "/libraries/sky130_fd_sc_hd/latest/cells/*/")


outfilename = 'view-standard/stdcells.v'
infilenames = []

for cell_dir in cell_dirs:
    libname = cell_dir.split('/')[-5]
    cellname = cell_dir.split('/')[-2]

    # Main top level verilog + other sizes
    infilenames = infilenames + glob(cell_dir+libname+'__'+cellname+'.functional.v') + glob(cell_dir+libname+'__'+cellname+'_*.v')

write_concat_file(outfilename, infilenames)


outfilename = 'view-standard/stdcells.lef'
infilenames = []

for cell_dir in cell_dirs:
    libname = cell_dir.split('/')[-5]
    cellname = cell_dir.split('/')[-2]

    # LEF file for each size
    print(glob(cell_dir+libname+'__'+cellname+'_*.lef'))

    infilenames = infilenames + list(set(glob(cell_dir+libname+'__'+cellname+'_*.lef')) - set(glob(cell_dir+libname+'__'+cellname+'_*.magic.lef')))

print(infilenames)
write_concat_lef_file(outfilename, infilenames)


outfilename = 'view-standard/stdcells.cdl'
infilenames = []

for cell_dir in cell_dirs:
    libname = cell_dir.split('/')[-5]
    cellname = cell_dir.split('/')[-2]

    # CDL file for each size
    infilenames = infilenames + glob(cell_dir+libname+'__'+cellname+'_*.cdl')

write_concat_file(outfilename, infilenames)


outfilename = 'view-standard/stdcells.spi'
infilenames = []

for cell_dir in cell_dirs:
    libname = cell_dir.split('/')[-5]
    cellname = cell_dir.split('/')[-2]

    # Spice file for each size
    infilenames = infilenames + glob(cell_dir+libname+'__'+cellname+'_*.spice')

write_concat_file(outfilename, infilenames)


copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/tech/sky130_fd_sc_hd.tlef', 'view-standard/rtk-tech.lef')

# Lib files
#copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/timing/sky130_fd_sc_hd__tt_025C_1v80.lib', 'view-standard/stdcells.lib')
#copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/timing/sky130_fd_sc_hd__ss_100C_1v40.lib', 'view-standard/stdcells-wc.lib')
#copyfile(SKYWATER130_HOME + '/libraries/sky130_fd_sc_hd/latest/timing/sky130_fd_sc_hd__ff_n40C_1v95.lib', 'view-standard/stdcells-bc.lib')

# Convert libs to dbs

#calibre-drc-block.rule
#calibre.layerprops
#calibre-lvs.rule
#display.drf
#klayout.lyp
#rtk-stream-out.map
#rtk-tech.info

#rtk-tech.par
#rtk-tech.tf
#rtk-typical.captable

# Needs special processing
#stdcells.gds

# Need to create with Synopsys tools
#stdcells.db
#stdcells.mwlib
