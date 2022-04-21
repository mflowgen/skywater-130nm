read_lef \
  -lib_name stdcells.mwlib \
  -cell_lef_files ../view-standard/stdcells.lef \
  -tech_lef_files ../view-standard/rtk-tech.lef

write_mw_lib_files -technology -output rtk-tech.tf stdcells.mwlib

exit
